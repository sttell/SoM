# -*- coding: utf-8 -*-
# You are using an open source project
# Date when the first version of this module was created: 09.06.2020 6:30 AM
# Date when the module was last edited: 13.06.2020 9:21 AM
# The Creator is not responsible for any changes made by a third party developer
# Author: Biro Ilya. St.Tell MAIL:st.tell@mail.ru Russia, Moscow

from PyQt5 import QtWidgets
import matplotlib.pyplot as plt
import numpy as np
import time
import os


class P(object):
    """
    This class describes the load object: the transverse point load.
    """
    def __init__(self, x: float, value: float):
        # Coordinate of the application point
        self.x = x
        # The value in kiloNewtons(kN)
        self.val = value

    def form_q(self, coord: float) -> float:
        """
        Calculates the effect of this object on the graph Q at the calculation point.
        :param coord: The coordinate where the calculation is performed
        :return: Coefficient of influence on the graph Q
        """
        if coord >= self.x:
            return self.val
        return 0.0

    def form_m(self, coord: float, flag='building') -> float:
        """
        Calculates the effect of this object on the graph M at the calculation point.
        :param coord: The coordinate where the calculation is performed
        :param flag: In the development.
        :return: Coefficient of influence on the graph M.
        """
        if flag == 'building' and coord >= self.x:
            return self.val * (coord - self.x)
        return 0.0

    def form_phi(self, coord: float) -> float:
        """
        Calculates the effect of this object on the graph Phi at the calculation point.
        :param coord: The coordinate where the calculation is performed
        :return: Coefficient of influence on the graph Phi
        """
        if self.x <= coord:
            return -self.val * (coord - self.x) ** 2 * 0.5
        return 0.0

    def form_v(self, coord: float) -> float:
        """
        Calculates the effect of this object on the graph V at the calculation point.
        :param coord: The coordinate where the calculation is performed
        :return: Coefficient of influence on the graph V
        """
        if coord >= self.x:
            return -self.val * (coord - self.x) ** 3 / 6
        return 0.0

    def reac(self, reaction) -> float:
        """
        Used for calculating the reaction coefficients in the beam support.
        :param reaction: The reaction is represented as an object P with a support coordinate.
        :return: Coefficient of influence of the object.
        """
        if self.x < reaction.x:
            return -self.val * (reaction.x - self.x)
        elif self.x > reaction.x:
            return self.val * (self.x - reaction.x)
        else:
            return 0.0


class M(object):
    # Describes the load: bending moment.
    def __init__(self, x: float, value: float):
        self.x = x
        self.val = value

    @staticmethod
    def form_q(container: float, coord=1) -> float:
        """
        Static method. The bending moment object does not affect the Q graph.
        :param container: Takes the coordinate value.
        :param coord: You don't have to take anything
        :return: Returns a zero coefficient.
        """
        return 0.0

    def form_m(self, coord: float, flag='building') -> float:
        """
        Describes the effect of an object of type M on the graph M.
        :param coord: Takes the value of the coordinate of the calculation point.
        :param flag: In the development.
        :return: Сoefficient of influence or zero.
        """
        if flag == 'building' and coord >= self.x:
            return -self.val
        return 0.0

    def form_phi(self, coord: float) -> float:
        """
        Describes the effect of an object of type M on the graph Phi.
        :param coord: Takes the value of the coordinate of the calculation point.
        :return: Сoefficient of influence or zero.
        """
        if coord >= self.x:
            return self.val * (coord - self.x)
        return 0.0

    def form_v(self, coord) -> float:
        """
        Describes the effect of an object of type M on the graph V.
        :param coord: Takes the value of the coordinate of the calculation point.
        :return: Сoefficient of influence or zero.
        """
        if coord >= self.x:
            return self.val * (coord - self.x) ** 2 / 2
        return 0.0

    def reac(self, reaction) -> float:
        """
        Used for calculating the reaction coefficients in the beam support.
        :param reaction: The reaction is represented as an object P with a support coordinate.
        :return: Coefficient of influence of the object.
        """
        return self.val


class Q(object):
    # Describes the behavior of the load:
    # Distributed load under transverse impact.
    def __init__(self, start: float, end: float, value: float):
        # Beginning of the impact area
        self.start = start
        # End of the impact area
        self.end = end
        # Value in kN/m
        self.q = value
        # Interpolates the Q object and gets values in the point load representation
        self.x = (self.end - self.start) / 2 + self.start
        self.val = value * (self.end - self.start)

    def form_q(self, coord: float) -> float:
        """
        Describes the effect of an object of type Q on the graph Q.
        :param coord: Takes the value of the coordinate of the calculation point.
        :return: Сoefficient of influence or zero.
        """
        if self.start <= coord <= self.end:
            return self.q * (coord - self.start)
        elif self.end < coord:
            return self.q * (coord - self.start) - self.q * (coord - self.end)
        else:
            return 0

    def form_m(self, coord: float, flag='building') -> float:
        """
        Describes the effect of an object of type Q on the graph M.
        :param coord: Takes the value of the coordinate of the calculation point.
        :param flag: In the development.
        :return: Сoefficient of influence or zero.
        """
        if flag == 'building':
            if self.start <= coord <= self.end:
                return self.q * (coord - self.start) ** 2 * 0.5
            elif self.end < coord:
                return self.q * 0.5 * ((coord - self.start) ** 2 - (coord - self.end) ** 2)
            return 0

    def form_phi(self, coord: float) -> float:
        """
        Describes the effect of an object of type Q on the graph Phi.
        :param coord: Takes the value of the coordinate of the calculation point.
        :return: Сoefficient of influence or zero.
        """
        if self.start <= coord <= self.end:
            return -self.q * (coord - self.start) ** 3 / 6
        elif self.end < coord:
            return -self.q / 6 * ((coord - self.start) ** 3 - (coord - self.end) ** 3)
        return 0

    def form_v(self, coord: float) -> float:
        """
        Describes the effect of an object of type Q on the graph V.
        :param coord: Takes the value of the coordinate of the calculation point.
        :return: Сoefficient of influence or zero.
        """
        if self.start <= coord <= self.end:
            return -self.q * (coord - self.start) ** 4 / 24
        elif self.end < coord:
            return -self.q / 24 * ((coord - self.start) ** 4 - (coord - self.end) ** 4)
        return 0

    def reac(self, reaction):
        """
        Used for calculating the reaction coefficients in the beam support.
        :param reaction: The reaction is represented as an object P with a support coordinate.
        :return: Coefficient of influence of the object or zero.
        """
        if self.x < reaction.x:
            return -self.val * (reaction.x - self.x)
        elif self.x > reaction.x:
            return self.val * (self.x - reaction.x)
        else:
            return 0


class Solver(object):
    # Class responsible for performing calculations in the task.
    def __init__(self, out_window: QtWidgets.QTextBrowser):
        # Output window object
        self.out_window = out_window

        # In the future it will take the boolean value
        # Updated in the _unpack_settings method
        self.create_q = None
        self.create_m = None
        self.create_phi = None
        self.create_v = None
        self.sing_points = None
        self.show_extr = None
        self.user_points = None
        self.out_file = None
        self.out_gui = None
        self.create_graph = None
        # In the future it will take the string value
        self.image_dir = None
        self.file_dir = None
        self.image_fmt = None

        # Variables that are responsible for setting the task
        # Updated in the _unpack_task method
        self.load_list = None
        self.reaction_coord = None
        self.hingles_list = None
        self.beam_lenght = None
        self.elastic = None
        self.inertion = None
        self.reac_type = None
        self.eps = 0.001
        self.phi0 = 0
        self.v0 = 0

    def run_solver(self, task_params: dict, settings_params: dict) -> None:
        """
        Method that starts the solution.
        :param task_params: Dictionary with a Packed task.
        :param settings_params: The dictionary is Packed with settings.
        :return: Nothing.
        """
        # Method for unpacking settings
        self._unpack_settings(settings_params)
        # Method for unpacking an issue
        self._unpack_task(task_params)
        # The method of calculating the reactions
        self._calc_reactions()
        # Method for calculating initial parameters
        self._calc_init_condition()
        # Method that forms the output
        self._get_solution()

    def _unpack_settings(self, settings_params: dict) -> None:
        """
        The method unpacks the dictionary with settings
        and assigns corresponding values to the class attributes.
        :param settings_params: The dictionary is Packed with settings.
        :return: Nothing.
        """
        self.create_q = settings_params["CREATE_Q"]
        self.create_m = settings_params["CREATE_M"]
        self.create_phi = settings_params["CREATE_PHI"]
        self.create_v = settings_params["CREATE_V"]
        self.sing_points = settings_params["SINGULAR_POINTS"]
        self.show_extr = settings_params["SHOW_EXTR"]
        self.user_points = settings_params["USER_POINTS"]
        self.out_file = settings_params["OUT_FILE"]
        self.out_gui = settings_params["OUT_GUI"]
        self.create_graph = settings_params["CREATE_GRAPHICS"]
        self.image_dir = settings_params["IMAGE_DIR"]
        self.file_dir = settings_params["FILE_DIR"]
        self.image_fmt = settings_params["IMAGE_FMT"]
        self.eps = settings_params["EPS"]

    def _unpack_task(self, task_params: dict) -> None:
        """
        The method unpacks the dictionary with settings
        and assigns corresponding values to the class attributes.
        :param task_params: The dictionary is Packed with task parameters.
        :return: Nothing.
        """
        self.load_list = task_params["FORCES"]
        self.reaction_coord = task_params["REACTIONS"]
        self.hingles_list = task_params["HINGHLES"]
        self.user_points_coords = task_params["USER_POINTS"]
        self.beam_lenght = task_params["BEAM_LENGHT"]
        self.elastic = task_params["ELASTIC_MODULE"]
        self.inertion = task_params["INERTION_MOMENT"]
        self.reac_type = task_params["REACTION_TYPE"]

        # Replacing string variables in the list of reaction coordinates with floating point numbers
        if len(self.reaction_coord) == 2:
            self.reaction_coord = [float(self.reaction_coord[0]), float(self.reaction_coord[1])]
        else:
            self.reaction_coord = [float(self.reaction_coord[0])]

    def _calc_reactions(self):
        """
        Calculates the values of the support reactions according to the type of beam attachment.
        :return: Nothing.
        """
        # Determination of reactions with two hinged supports
        if len(self.reaction_coord) == 2:
            r_a = P(self.reaction_coord[0], 0)
            r_b = P(self.reaction_coord[1], 0)
            reac = 0
            for force in self.load_list:
                reac += force.reac(r_a)
            r_b.val = - reac / abs(r_a.x - r_b.x)
            reac = 0
            self.load_list.append(r_b)
            for force in self.load_list:
                if type(force) != M:
                    reac += force.val
            r_a.val = -reac
            self.load_list.append(r_a)
            del r_a, r_b, reac
        # Determination of reactions with a single support-seal
        if len(self.reaction_coord) == 1:
            reac = P(0, 0.0)
            mom = M(0, 0.0)
            reac_val = 0
            for force in self.load_list:
                if type(force) != M:
                    reac_val += force.val
            reac.val = - reac_val
            m_v = 0
            for force in self.load_list:
                m_v += force.reac(reac)
            mom.val = - m_v
            self.load_list.append(reac)
            self.load_list.append(mom)
            del reac, mom, m_v, reac_val

    def _calc_init_condition(self) -> None:
        """
        Defines the initial parameters of the problem:
        The angle of rotation and Deflection of the beam at the point x=0
        :return:
        """
        # Calculations for the type of supports: Articulated beam
        if len(self.reaction_coord) == 2:
            b1 = 0
            b2 = 0
            for force in self.load_list:
                b1 += force.form_v(self.reaction_coord[0])
                b2 += force.form_v(self.reaction_coord[1])
            mtrx = np.array([[1, self.reaction_coord[0]],
                             [1, self.reaction_coord[1]]])
            v1 = np.array([-b1, -b2])
            vector = np.linalg.solve(mtrx, v1)
            self.v0 = vector[0]
            self.phi0 = vector[1]
            del b1, b2, mtrx, v1, vector
        # Calculations for the type of supports: Sealing
        if len(self.reaction_coord) == 1:
            # The values remain null because of the physical meaning
            pass

    def _get_solution(self) -> None:
        """
        The main method responsible for calculating
        the problem with the set conditions and settings.
        :return: Nothing
        """

        # Lists for further storage of the solution.
        # List with coordinates of calculation points.
        x_coords = []
        # A list with the graph values of bending moments.
        m_values = []
        # List with Q graph values.
        q_values = []
        # A list with the values of the graph of deflection
        v_values = []
        # List with the values of the graph of rotation angles of the section
        phi_values = []
        # Step which is the calculation
        dx = self.eps
        # The number of steps for solving the problem with the specified accuracy
        num_steps = pow(self.eps, -1)
        # Variable for further storage of output text.
        rn = len(str(dx)) - 2  # Round number
        text = f"""------> Произведен запуск вычислений. <------
Параметры задачи:
Точность вычислений - {self.eps}
Тип опор в задаче: {self.reac_type}
Количество заданных опор: {len(self.reaction_coord)}
Количество заданных нагрузрок: {len(self.load_list)}
Количество шарниров: {len(self.hingles_list)}

Доп информация по решению ниже.

"""
        # Calculation cycle
        start_time = time.time()

        # Searches for values in user points
        if self.user_points and len(self.user_points_coords) != 0:
            # Initialize lists to hold the values
            q_points_val = list()
            m_points_val = list()
            phi_points_val = list()
            v_points_val = list()

            for p_coord in self.user_points_coords:
                # Initialize variables to hold the values
                p_q = 0
                p_m = 0
                p_phi = self.phi0  # Initial conditions method
                p_v = self.v0 + self.phi0 * p_coord  # Initial conditions method

                # Search for values
                for load in self.load_list:
                    p_q += load.form_q(coord=p_coord) / (self.elastic * self.inertion)
                    p_m += load.form_m(coord=p_coord) / (self.elastic * self.inertion)
                    p_phi += load.form_phi(coord=p_coord) / (self.elastic * self.inertion)
                    p_v += load.form_v(coord=p_coord) / (self.elastic * self.inertion)

                # Added values
                q_points_val.append(round(p_q, rn))
                m_points_val.append(round(p_m, rn))
                phi_points_val.append(round(p_phi, rn))
                v_points_val.append(round(p_v, rn))

            # Set OutWindow text
            text += '-----> Значения в точках пользователя <-----\n'
            # Counter
            ctr = 0

            for point in self.user_points_coords:
                points_text = f"""Значения в точке х={point} м:
Q(x)={q_points_val[ctr]}; M(x) = {m_points_val[ctr]}; Phi(x)={phi_points_val[ctr]}; V(x) = {v_points_val[ctr]}

"""
                ctr += 1
                text += points_text
            text += '\n'

            # Clear memory
            del p_q, p_v, p_phi, p_coord
            del q_points_val, m_points_val, v_points_val, phi_points_val
            del ctr, points_text

        # Main solution
        for x in [val / num_steps for val in range(0, int(self.beam_lenght * num_steps) + 1)]:
            ep_q = 0
            ep_m = 0
            ep_phi = self.phi0
            ep_v = self.v0 + self.phi0 * x

            for force in self.load_list:
                ep_q += force.form_q(x) / (self.elastic * self.inertion)
                ep_m += force.form_m(x) / (self.elastic * self.inertion)
                ep_phi += force.form_phi(x) / (self.elastic * self.inertion)
                ep_v += force.form_v(x) / (self.elastic * self.inertion)

            # Writes values to lists depending on the settings set by the user.
            x_coords.append(x)
            q_values.append(ep_q)
            m_values.append(ep_m)
            phi_values.append(ep_phi)
            v_values.append(ep_v)

            if self.out_file or self.out_gui:
                text += f'X={round(x, rn)} ; Q={round(ep_q, rn)} ; M={round(ep_m,rn)} ;' + \
                        f' Phi={round(ep_phi,rn)} ; V={round(ep_v,rn)} ;\n'
        end_time = time.time()
        # Output data to the user interface
        if self.out_gui:
            if self.show_extr:
                extr_point_text = \
                    f"""------> Максимальные значения в точках экстремума <------
Q(x): max({round(max(q_values), rn)}), min({round(min(q_values), rn)})
M(x): max({round(max(m_values), rn)}), min({round(min(m_values), rn)})
Phi(x): max({round(max(phi_values), rn)}, min({round(min(phi_values), rn)})
V(x): max({round(max(v_values), rn)}), min({round(min(v_values), rn)})
"""
                text += extr_point_text
            self.out_window.setText(text)
        # Output to file
        # The try-except construct is responsible
        # for intercepting an exception caused by the absence of a save directory. I
        # f it is not present, it creates a new one.
        try:
            if self.out_file:
                path = self.file_dir + '\\solution.txt'
                file = open(path, 'w', encoding='utf-8')
                text += f'Задача решена за {num_steps} шагов.'
                text += f'Время расчетов: {end_time-start_time} sec.\n'
                file.write(text)
                file.close()
        except FileNotFoundError:
            os.mkdir(self.file_dir)
            path = self.file_dir + '\\solution.txt'
            file = open(path, 'w', encoding='utf-8')
            text += f'Задача решена за {num_steps} шагов.'
            text += f'Время расчетов: {end_time - start_time} sec.\n'
            file.write(text)
            file.close()

            # Starts the process of creating load graphs.
            if self.create_graph:
                start_time = time.time()
                if self.create_q:
                    q = Epure(x_coords, q_values, self.image_dir, image_format=self.image_fmt, obj_name="Q")
                    q.set_eps(self.eps)
                    q.plot_graph(show_extr=self.show_extr)
                if self.create_m:
                    m = Epure(x_coords, m_values, self.image_dir, image_format=self.image_fmt, obj_name="M")
                    m.set_eps(self.eps)
                    m.plot_graph(show_extr=self.show_extr)
                if self.create_phi:
                    phi = Epure(x_coords, phi_values, self.image_dir, image_format=self.image_fmt, obj_name="Phi")
                    phi.set_eps(self.eps)
                    phi.plot_graph(show_extr=self.show_extr)
                if self.create_v:
                    v = Epure(x_coords, v_values, self.image_dir, image_format=self.image_fmt, obj_name="v")
                    v.set_eps(self.eps)
                    v.plot_graph(show_extr=self.show_extr)
                end_time = time.time()
                new_txt = self.out_window.toPlainText() + f'Время постоения графиков: {end_time - start_time}\n'
                self.out_window.setText(new_txt)
            # Clear memory
            del ep_v, ep_q, ep_phi, ep_m, v, phi, q, m
            del q_values, m_values, v_values, phi_values
            del path, rn, x_coords, x, num_steps, dx, start_time, end_time


class Epure(object):
    """
    Class Epure. Responsible for the graphical representation of lists.
    """

    def __init__(self, x_list, y_list, directory_path, image_format='png', obj_name=None):
        """
        :param x_list: x-coord values
        :param y_list: y-coord values
        :param directory_path: path to save directory
        :param obj_name: name object to assign a name to an image
        """
        self.x = x_list
        self.y = y_list
        self.normalisation()
        self.name = obj_name
        self.dir = directory_path
        self.fmt = image_format
        self.eps = 0.001

    def normalisation(self):
        """
        If the size of the input data does not match, it adds null values to the missing values
        :return: None
        """
        if len(self.x) == len(self.y):
            pass
        else:
            while len(self.x) != len(self.y):
                if len(self.x) < len(self.y):
                    self.x.append(0)
                else:
                    self.y.append(0)

    def set_eps(self, eps: float):
        """
        Sets the value of the precision build. By default, it is 0.001.
        :param eps: precision
        :return: None
        """
        self.eps = eps

    def plot_graph(self, show_extr=False):
        """
        Plotting a function
        :return: None
        """

        def get_rotation(y_coord):
            if y_coord <= 0:
                return -10
            else:
                return 10

        # Image parameters
        fig = plt.gcf()
        fig.set_size_inches(16.5, 8.5)

        # Zero line
        plt.plot(self.x, [0 for _ in range(len(self.x))], c='black')

        # Vertical lines (Ordinates)
        x_index = 0
        for x in self.x:
            if x == 0.0:
                plt.plot([0, 0], [0, self.y[0]], c='black')
            elif round((x * (25 / max(self.x))) % 1, 4) == 0.0:
                plt.plot([x, x], [0, self.y[x_index]], c='black')
            x_index += 1

        # Main Line
        plt.plot(self.x, self.y, c='Red')

        # Titles
        plt.title('Эпюра ' + self.name + '(x)')
        plt.xlabel('x-coord')
        plt.ylabel(self.name + ' value')

        # Set Grid
        plt.grid()
        # Plotting point extr
        if show_extr:
            # Marks the extreme points on the chart.

            y = np.array(self.y)
            x = np.array(self.x)

            # Max point
            i = np.unravel_index(y.argmax(), y.shape)
            x_pos = x[i]
            y_max = np.max(y)

            # The mask is created in the EPS neighborhood of the extreme point
            if y_max >= 0:
                mask = y > (y_max - self.eps)
            else:
                mask = y < (y_max + self.eps)

            plt.scatter(x[mask], y[mask], color='orange', s=40, marker='o')
            plt.text(x_pos, y_max, f'{round(y_max, 4)}', rotation=get_rotation(y_max))

            # Min point
            i = np.unravel_index(y.argmin(), y.shape)
            x_pos = x[i]
            y_min = np.min(y)

            # The mask is created in the EPS neighborhood of the extreme point
            if y_min <= 0:
                mask = y < (y_min + self.eps)
            else:
                mask = y > (y_min - self.eps)

            plt.scatter(x[mask], y[mask], color='orange', s=40, marker='o')
            plt.text(x_pos, y_min, f'{round(y_min, 4)}', rotation=get_rotation(y_min))

        # The try-except construct is responsible
        # for intercepting an exception caused by the absence of a save directory. I
        # f it is not present, it creates a new one.
        try:
            path = self.dir + f'\\{self.name}.{self.fmt}'
            plt.savefig(path)
        except FileNotFoundError:
            os.mkdir(self.dir)
            path = self.dir + f'\\{self.name}.{self.fmt}'
            plt.savefig(path)
        plt.close()
