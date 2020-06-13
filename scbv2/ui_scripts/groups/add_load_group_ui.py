# -*- coding: utf-8 -*-
# You are using an open source project
# Date when the first version of this module was created: 05.06.2020 7:00 AM
# Date when the module was last edited: 09.06.2020 1:16 AM
# The Creator is not responsible for any changes made by a third party developer
# Author: Biro Ilya. St.Tell MAIL:st.tell@mail.ru Russia, Moscow

from PyQt5 import QtCore, QtWidgets
from scbv2.solver import Q, M, P


class AddLoadGroup(object):
    # The class initializes the load input field
    def __init__(self,
                 menu: QtWidgets.QWidget,
                 main_window: QtWidgets.QWidget):
        _translate = QtCore.QCoreApplication.translate
        # Lists parameters
        self.load_list = list()
        self.reaction_list = list()
        self.hinge_list = list()
        """
        INIT UNITS
        """
        self._load_params_window = QtWidgets.QTextBrowser(menu)
        self._load_params_window.setGeometry(QtCore.QRect(10, 250, 381, 171))
        self._load_params_window.setObjectName("_load_params_window")

        self._init_labels(menu, _translate)
        self._init_btn(menu, _translate)
        self._init_input_boxes(menu)
        self._init_combo_boxes(menu, _translate)
        """
        INPUT BOXES LOGIC
        """
        # None logic
        """
        BUTTONS LOGIC
        """
        self._clear_all_param_btn.clicked.connect(
            lambda obj, lw=self._load_params_window: self.clr_load_panel(lw)
        )
        self._clear_last_param_btn.clicked.connect(
            lambda obj, lw=self._load_params_window: self.clr_last_load_panel(lw)
        )
        self._add_load_btn.clicked.connect(
            lambda obj, mw=main_window: self._add_load(mw)
        )
        """
        COMBO BOXES LOGIC
        """
        self.select_load_inp.currentIndexChanged.connect(self._set_inp_load)

    def _init_labels(self,
                     menu: QtWidgets.QWidget,
                     _translate: QtCore.QCoreApplication.translate) -> None:
        """
        Initializes labels
        :param menu: Solver menu
        :param _translate: Translator
        :return: None
        """
        self._add_load_lab = QtWidgets.QLabel(menu)
        self._add_load_lab.setGeometry(QtCore.QRect(10, 490, 81, 25))
        self._add_load_lab.setObjectName("_add_load_lab")
        self._add_load_lab.setText(_translate("MainWindow", "Добавить:"))

        self._point_1_mtrc = QtWidgets.QLabel(menu)
        self._point_1_mtrc.setGeometry(QtCore.QRect(75, 580, 55, 16))
        self._point_1_mtrc.setObjectName("_point_1_mtrc")
        self._point_1_mtrc.setText(_translate("MainWindow", "м"))

        self._point_1_lab = QtWidgets.QLabel(menu)
        self._point_1_lab.setGeometry(QtCore.QRect(10, 540, 150, 21))
        self._point_1_lab.setObjectName("_point_1_lab")
        self._point_1_lab.setText(_translate("MainWindow", "Точка приложения:"))

        self._point_2_lab = QtWidgets.QLabel(menu)
        self._point_2_lab.setGeometry(QtCore.QRect(190, 540, 121, 21))
        self._point_2_lab.setObjectName("_point_2_lab")
        self._point_2_lab.hide()
        self._point_2_lab.setText(_translate("MainWindow", "Конец участка:"))

        self._point_2_mtrc = QtWidgets.QLabel(menu)
        self._point_2_mtrc.setGeometry(QtCore.QRect(255, 580, 55, 16))
        self._point_2_mtrc.setObjectName("_point_2_mtrc")
        self._point_2_mtrc.hide()
        self._point_2_mtrc.setText(_translate("MainWindow", "м"))

        self._value_lab = QtWidgets.QLabel(menu)
        self._value_lab.setGeometry(QtCore.QRect(10, 600, 121, 21))
        self._value_lab.setObjectName("_value_lab")
        self._value_lab.setText(_translate("MainWindow", "Значение:"))

        self._value_mtrc = QtWidgets.QLabel(menu)
        self._value_mtrc.setGeometry(QtCore.QRect(75, 640, 55, 16))
        self._value_mtrc.setObjectName("_value_mtrc")
        self._value_mtrc.setText(_translate("MainWindow", "кН"))

        self._loads_params_lab = QtWidgets.QLabel(menu)
        self._loads_params_lab.setGeometry(QtCore.QRect(10, 210, 391, 30))
        self._loads_params_lab.setObjectName("_loads_params_lab")
        self._loads_params_lab.setText(_translate("MainWindow", "Параметры нагрузок и опор:"))

    def _init_btn(self,
                  menu: QtWidgets.QWidget,
                  _translate: QtCore.QCoreApplication.translate) -> None:
        """
        Initializes buttons
        :param menu: Solver menu
        :param _translate: Translator
        :return: None
        """
        self._clear_all_param_btn = QtWidgets.QPushButton(menu)
        self._clear_all_param_btn.setGeometry(QtCore.QRect(10, 430, 181, 30))
        self._clear_all_param_btn.setObjectName("_clear_all_param_btn")
        self._clear_all_param_btn.setText(_translate("MainWindow", "Удалить все"))

        self._clear_last_param_btn = QtWidgets.QPushButton(menu)
        self._clear_last_param_btn.setGeometry(QtCore.QRect(200, 430, 191, 30))
        self._clear_last_param_btn.setObjectName("_clear_last_param_btn")
        self._clear_last_param_btn.setText(_translate("MainWindow", "Удалить последнее"))

        self._add_load_btn = QtWidgets.QPushButton(menu)
        self._add_load_btn.setGeometry(QtCore.QRect(190, 630, 180, 27))
        self._add_load_btn.setObjectName("_add_load_btn")
        self._add_load_btn.setText(_translate("MainWindow", "Добавить"))

    def _init_input_boxes(self,
                          menu: QtWidgets.QWidget) -> None:
        """
        Initializes input boxes
        :param menu: Solver menu
        :return: None
        """
        self.point_1_inp = QtWidgets.QLineEdit(menu)
        self.point_1_inp.setGeometry(QtCore.QRect(10, 570, 60, 27))
        self.point_1_inp.setObjectName("point_1_inp")

        self.point_2_inp = QtWidgets.QLineEdit(menu)
        self.point_2_inp.setGeometry(QtCore.QRect(190, 570, 60, 27))
        self.point_2_inp.setObjectName("point_2_inp")
        self.point_2_inp.hide()

        self.value_inp = QtWidgets.QLineEdit(menu)
        self.value_inp.setGeometry(QtCore.QRect(10, 630, 60, 27))
        self.value_inp.setObjectName("value_inp")

    def _init_combo_boxes(self,
                          menu: QtWidgets.QWidget,
                          _translate: QtCore.QCoreApplication.translate) -> None:
        """
        Initializes combo boxes
        :param menu: Solver menu
        :param _translate: Translator
        :return: None
        """
        self.select_load_inp = QtWidgets.QComboBox(menu)
        self.select_load_inp.setGeometry(QtCore.QRect(90, 490, 151, 26))
        self.select_load_inp.setObjectName("select_load_inp")
        self.select_load_inp.addItem("")
        self.select_load_inp.addItem("")
        self.select_load_inp.addItem("")
        self.select_load_inp.addItem("")
        self.select_load_inp.addItem("")

        self.select_load_inp.setItemText(0, _translate("MainWindow", "Сила(P)"))
        self.select_load_inp.setItemText(1, _translate("MainWindow", "Момент(М)"))
        self.select_load_inp.setItemText(2, _translate("MainWindow", "Распр.Нагрузка(Q)"))
        self.select_load_inp.setItemText(3, _translate("MainWindow", "Опора"))
        self.select_load_inp.setItemText(4, _translate("MainWindow", "Врезанный шарнир"))

    def _set_inp_load(self) -> None:
        """
        This method is called when the user changes the combo box "select_load_inp" state.
        Changes the visibility of widgets according to the required parameters.
        :return: None
        """
        if self.select_load_inp.currentText() == 'Сила(P)':
            self._point_1_lab.setText('Точка приложения:')
            self.point_2_inp.hide()
            self._point_2_mtrc.hide()
            self._point_2_lab.hide()
            self.value_inp.show()
            self._value_lab.show()
            self._value_mtrc.show()
            self._value_mtrc.setText('kH')
            self.point_2_inp.clear()
            self.point_1_inp.clear()
            self.value_inp.clear()
        elif self.select_load_inp.currentText() == "Момент(М)":
            self._point_1_lab.setText('Точка приложения:')
            self.point_2_inp.hide()
            self._point_2_mtrc.hide()
            self._point_2_lab.hide()
            self.value_inp.show()
            self._value_lab.show()
            self._value_mtrc.show()
            self._value_mtrc.setText('kHм')
            self.point_2_inp.clear()
            self.point_1_inp.clear()
            self.value_inp.clear()
        elif self.select_load_inp.currentText() == "Распр.Нагрузка(Q)":
            self._point_1_lab.setText('Начало участка:')
            self.point_2_inp.show()
            self._point_2_mtrc.show()
            self._point_2_lab.show()
            self.value_inp.show()
            self._value_lab.show()
            self._value_mtrc.show()
            self._value_mtrc.setText('kH/м')
            self.point_2_inp.clear()
            self.point_1_inp.clear()
            self.value_inp.clear()
        elif self.select_load_inp.currentText() == "Опора":
            self._point_1_lab.setText('Точка опоры:')
            self.point_2_inp.hide()
            self._point_2_mtrc.hide()
            self._point_2_lab.hide()
            self.value_inp.hide()
            self._value_lab.hide()
            self._value_mtrc.hide()
            self.point_2_inp.clear()
            self.point_1_inp.clear()
            self.value_inp.clear()
        elif self.select_load_inp.currentText() == "Врезанный шарнир":
            self._point_1_lab.setText('Координаты:')
            self.point_2_inp.hide()
            self._point_2_mtrc.hide()
            self._point_2_lab.hide()
            self.value_inp.hide()
            self._value_lab.hide()
            self._value_mtrc.hide()
            self.point_2_inp.clear()
            self.point_1_inp.clear()
            self.value_inp.clear()

    def _add_load(self,
                  main_window: QtWidgets.QMainWindow) -> None:
        """
        Method called when the add button is clicked.
        Collects the load parameters entered by the user,
        checks their correctness, outputs either an error message,
        or adds information to the output field.
        :param main_window: Main Window object.
        :return: None
        """
        def add_to_window(obj: QtWidgets.QTextBrowser, text: str) -> None:
            """
            Adding a user-entered load to the load output window.
            :param obj: Output Window
            :param text: Output Text
            :return: None
            """
            data = obj.toPlainText().split('\n')
            if data[0] != '':
                data.append(text)
                obj.setText('\n'.join(data))
            else:
                obj.setText(text)
            del data

        def check_correct_loads(value: str) -> bool:
            """
            Checks whether the load parameters entered by the user are correct.
            :param value: Value in string form
            :return: If correct - True, if not correct - False
            """
            try:
                check = float(value.rstrip().lstrip().replace(',', '.'))
                return True
            except ValueError:
                return False

        def check_correct_reac(value: str) -> bool:
            """
            Checks whether the load parameters entered by the user are correct.
            :param value: Value in string form
            :return: If correct - True, if not correct - False
            """
            try:
                check = float(value.rstrip().lstrip().replace(',', '.'))
                if check >= 0:
                    return True
                else:
                    raise ValueError
            except ValueError:
                return False

        def clear_text(value: str) -> str:
            """
            Clears the user-entered value from unnecessary spaces,
            and replaces the user-entered number form with a Python-supported one,
            if necessary.
            :param value: Float value in string form
            :return: Cleared value
            """
            return value.rstrip().lstrip().replace(',', '.')

        if self.select_load_inp.currentText() == 'Сила(P)':
            if check_correct_loads(self.point_1_inp.text()) and\
               check_correct_loads(self.value_inp.text()):
                coord = clear_text(self.point_1_inp.text())
                val = clear_text(self.value_inp.text())
                load = f'P({coord}, {val})'
                add_to_window(self._load_params_window, load)
                self.load_list.append(P(float(coord), float(val)))
            else:
                self.error_box(main_window, 'Введенное значение не корректно.', 'Ошибка')

        elif self.select_load_inp.currentText() == "Момент(М)":
            if check_correct_loads(self.point_1_inp.text()) and\
               check_correct_loads(self.value_inp.text()):
                coord = clear_text(self.point_1_inp.text())
                val = clear_text(self.value_inp.text())
                load = f'M({coord}, {val})'
                add_to_window(self._load_params_window, load)
                self.load_list.append(M(float(coord), float(val)))
            else:
                self.error_box(main_window, 'Введенное значение не корректно.', 'Ошибка')

        elif self.select_load_inp.currentText() == "Распр.Нагрузка(Q)":
            if check_correct_loads(self.point_1_inp.text()) and\
               check_correct_loads(self.value_inp.text()) and\
               check_correct_loads(self.point_2_inp.text()):
                try:
                    start = clear_text(self.point_1_inp.text())
                    end = clear_text(self.point_2_inp.text())
                    if float(start) < float(end):
                        val = clear_text(self.value_inp.text())
                        load = f'Q({start}, {end}, {val})'
                        add_to_window(self._load_params_window, load)
                        self.load_list.append(Q(float(start), float(end), float(val)))
                    else:
                        self.error_box(main_window,
                                       'Введенное значение не корректно. Начало дальше чем конец.',
                                       'Ошибка')
                except ValueError:
                    print('тут')
            else:
                self.error_box(main_window, 'Введенное значение не корректно.', 'Ошибка')

        elif self.select_load_inp.currentText() == "Опора":
            if check_correct_reac(self.point_1_inp.text()):
                coord = clear_text(self.point_1_inp.text())
                load = f'Опора в точке {coord} м'
                add_to_window(self._load_params_window, load)
                self.reaction_list.append(self.point_1_inp.text())
            else:
                self.error_box(main_window, 'Введенное значение не корректно.', 'Ошибка')

        elif self.select_load_inp.currentText() == "Врезанный шарнир":
            if check_correct_reac(self.point_1_inp.text()):
                coord = clear_text(self.point_1_inp.text())
                load = f'Врезанный шарнир в точке {coord} м'
                add_to_window(self._load_params_window, load)
                self.hinge_list.append(self.point_1_inp.text())
            else:
                self.error_box(main_window, 'Введенное значение не корректно.', 'Ошибка')

    def get_data(self) -> (list, list, list):
        """
        Returns data entered by the user collected during the entire program execution.
        :return: Load list, Reaction list, Hinge list
        """
        return self.load_list, self.reaction_list, self.hinge_list

    def clr_last_load_panel(self, window: QtWidgets.QTextBrowser) -> None:
        """
        Deletes the last load element added by the user.
        :param window: output window for entered loads.
        :return: None
        """
        data = window.toPlainText().split('\n')
        window.setText('\n'.join(data[:-1]))
        if data[-1].startswith('P') or \
           data[-1].startswith('M') or \
           data[-1].startswith('Q'):
            self.load_list.pop()
        elif data[-1].startswith('Шарнир'):
            self.hinge_list.pop()
        elif data[-1].startswith('Опора'):
            self.reaction_list.pop()
        del data

    def clr_load_panel(self, window: QtWidgets.QTextBrowser) -> None:
        """
        Completely clears all data entered by the user in the load menu.
        :param window: output window for entered loads.
        :return: None
        """
        self.reaction_list = []
        self.load_list = []
        self.hinge_list = []
        window.clear()

    @staticmethod
    def error_box(main_window: QtWidgets.QWidget,
                  msg: str,
                  title: str) -> None:
        """
        Creating a pop-up error window.
        :param main_window: Main Window object
        :param msg: message
        :param title: message title
        :return: None
        """
        QtWidgets.QMessageBox.critical(main_window, title, msg)
