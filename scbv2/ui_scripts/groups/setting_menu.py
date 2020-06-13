# -*- coding: utf-8 -*-
# You are using an open source project
# Date when the first version of this module was created: 05.06.2020 7:00 AM
# Date when the module was last edited: 13.06.2020 9:23 AM
# The Creator is not responsible for any changes made by a third party developer
# Author: Biro Ilya. St.Tell MAIL:st.tell@mail.ru Russia, Moscow

from PyQt5 import QtWidgets, QtCore, QtGui
import easygui
import json as js
import os

# Path to the file with the latest user settings.
SETTING_PATH = str(os.getcwd()) + '\\scbv2\\setting.json'


class SettingMenu(object):
    # Class that creates the settings menu object.
    def __init__(self,
                 menu: QtWidgets.QWidget,
                 layouts_widgets: list,
                 layouts: dict):
        _translate = QtCore.QCoreApplication.translate
        self._init_check_boxes(layouts_widgets, layouts, _translate)
        self._init_lables(menu, _translate)
        self._init_input_boxes(menu, _translate)
        self._init_combo_boxes(menu, _translate)
        self._init_btns(menu, _translate)
        self._load_settings()

        self.directory_finder_image.clicked.connect(
            lambda obj, line=self.image_dir_inp: self.dir_find(line)
        )
        self.directory_finder_file.clicked.connect(
            lambda obj, line=self.file_directory_inp: self.dir_find(line)
        )
        self.set_default_settings_btn.clicked.connect(self._set_default_settings)
        self.set_settings_btn.clicked.connect(self._set_settings)

    def _init_check_boxes(self,
                          layouts_widgets: list,
                          layouts: dict,
                          _translate: QtCore.QCoreApplication.translate) -> None:
        """
        Initialization of CheckBox objects and subsequent translation to the main application window.
        :param layouts_widgets: The layout widget.
        :param layouts: The layout object.
        :param _translate: Translator.
        :return: None
        """
        self.create_q = QtWidgets.QCheckBox(layouts_widgets[0])
        self.create_q.setObjectName("create_q")
        layouts[layouts_widgets[0]].addWidget(self.create_q)
        self.create_q.setText(_translate("MainWindow", "Построение эпюры Q(x)"))

        self.create_m = QtWidgets.QCheckBox(layouts_widgets[0])
        self.create_m.setObjectName("create_m")
        layouts[layouts_widgets[0]].addWidget(self.create_m)
        self.create_m.setText(_translate("MainWindow", "Построение эпюры M(x)"))

        self.create_phi = QtWidgets.QCheckBox(layouts_widgets[0])
        self.create_phi.setObjectName("create_phi")
        layouts[layouts_widgets[0]].addWidget(self.create_phi)
        self.create_phi.setText(_translate("MainWindow", "Построение эпюры Phi(x)"))

        self.create_v = QtWidgets.QCheckBox(layouts_widgets[0])
        self.create_v.setObjectName("create_v")
        layouts[layouts_widgets[0]].addWidget(self.create_v)
        self.create_v.setText(_translate("MainWindow", "Построение эпюры V(x)"))

        self.singular_point = QtWidgets.QCheckBox(layouts_widgets[0])
        self.singular_point.setObjectName("singular_point")
        layouts[layouts_widgets[0]].addWidget(self.singular_point)
        self.singular_point.setText(_translate("MainWindow", "Показать значения в особых точках"))
        self.singular_point.setEnabled(False)

        self.show_extr = QtWidgets.QCheckBox(layouts_widgets[0])
        self.show_extr.setObjectName("show_extr")
        layouts[layouts_widgets[0]].addWidget(self.show_extr)
        self.show_extr.setText(_translate("MainWindow", "Показать точки экстремума на графиках"))

        self.find_user_points = QtWidgets.QCheckBox(layouts_widgets[0])
        self.find_user_points.setObjectName("find_user_points")
        layouts[layouts_widgets[0]].addWidget(self.find_user_points)
        self.find_user_points.setText(_translate("MainWindow", "Найти значения в точках пользователя"))

        self.out_file = QtWidgets.QCheckBox(layouts_widgets[1])
        self.out_file.setObjectName("out_file")
        layouts[layouts_widgets[1]].addWidget(self.out_file)
        self.out_file.setText(_translate("MainWindow", "Вывод результатов вычислений в файл"))

        self.out_GUI = QtWidgets.QCheckBox(layouts_widgets[1])
        self.out_GUI.setObjectName("out_GUI")
        layouts[layouts_widgets[1]].addWidget(self.out_GUI)
        self.out_GUI.setText(_translate("MainWindow", "Вывод результатов вычислений на панель"))

        self.create_graphics = QtWidgets.QCheckBox(layouts_widgets[1])
        self.create_graphics.setObjectName("create_graphics")
        layouts[layouts_widgets[1]].addWidget(self.create_graphics)
        self.create_graphics.setText(_translate("MainWindow", "Построить графики зависимостей"))

        self.create_image_directory = QtWidgets.QCheckBox(layouts_widgets[1])
        self.create_image_directory.setObjectName("create_image_directory")
        layouts[layouts_widgets[1]].addWidget(self.create_image_directory)
        self.create_image_directory.setText(_translate("MainWindow", "Создать папку Solution в директории вывода"))
        self.create_image_directory.clicked.connect(self._reload_dir)

    def _reload_dir(self) -> None:
        """
        When you click the CheckBox responsible for creating
        the directory reloads the path value in the input lines.
        :return: None
        """
        if self.file_directory_inp.text().endswith('Solution'):
            new_line = self.file_directory_inp.text().replace('\\Solution', '')
            self.file_directory_inp.setText(new_line)
            new_line = self.image_dir_inp.text().replace('\\Solution', '')
            self.image_dir_inp.setText(new_line)
            del new_line
        else:
            new_line = self.file_directory_inp.text() + '\\Solution'
            self.file_directory_inp.setText(new_line)
            new_line = self.image_dir_inp.text() + '\\Solution'
            self.image_dir_inp.setText(new_line)
            del new_line

    def _init_lables(self, 
                     menu: QtWidgets.QWidget, 
                     _translate: QtCore.QCoreApplication.translate) -> None:
        """
        Method for initializing labels objects in
        the main window and then translating the text.
        :param menu: tab menu -> settings menu.
        :param _translate: Translator.
        :return: None
        """
        self.solver_params_lab = QtWidgets.QLabel(menu)
        self.solver_params_lab.setGeometry(QtCore.QRect(20, 40, 231, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.solver_params_lab.setFont(font)
        self.solver_params_lab.setObjectName("solver_params_lab")
        self.solver_params_lab.setText(_translate("MainWindow", "Параметры решения:"))

        self.output_params_lab = QtWidgets.QLabel(menu)
        self.output_params_lab.setGeometry(QtCore.QRect(410, 40, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.output_params_lab.setFont(font)
        self.output_params_lab.setObjectName("output_params_lab")
        self.output_params_lab.setText(_translate("MainWindow", "Параметры вывода:"))

        self.image_dir_lab = QtWidgets.QLabel(menu)
        self.image_dir_lab.setGeometry(QtCore.QRect(410, 290, 301, 16))
        self.image_dir_lab.setObjectName("image_dir_lab")
        self.image_dir_lab.setText(_translate("MainWindow", "Директория для сохранения изображений:"))

        self.file_directory_lab = QtWidgets.QLabel(menu)
        self.file_directory_lab.setGeometry(QtCore.QRect(410, 360, 311, 16))
        self.file_directory_lab.setObjectName("file_directory_lab")
        self.file_directory_lab.setText(_translate("MainWindow", "Директория для сохранения файла вывода:"))

        self.set_eps_lab = QtWidgets.QLabel(menu)
        self.set_eps_lab.setGeometry(QtCore.QRect(20, 430, 161, 16))
        self.set_eps_lab.setObjectName("set_eps_lab")
        self.set_eps_lab.setText(_translate("MainWindow", "Точность вычислений:"))

        self.image_fmt_lab = QtWidgets.QLabel(menu)
        self.image_fmt_lab.setGeometry(QtCore.QRect(410, 430, 161, 16))
        self.image_fmt_lab.setObjectName("image_fmt_lab")
        self.image_fmt_lab.setText(_translate("MainWindow", "Формат изображений:"))
     
    def _init_input_boxes(self, 
                          menu: QtWidgets.QWidget, 
                          _translate: QtCore.QCoreApplication.translate) -> None:
        """
        Initializing input fields.
        :param menu: tab_menu -> settings menu
        :param _translate: translator.
        :return: None
        """
        self.file_directory_inp = QtWidgets.QLineEdit(menu)
        self.file_directory_inp.setGeometry(QtCore.QRect(410, 380, 431, 25))
        self.file_directory_inp.setObjectName("file_directory_inp")

        self.set_eps = QtWidgets.QLineEdit(menu)
        self.set_eps.setGeometry(QtCore.QRect(180, 425, 110, 25))
        self.set_eps.setObjectName("set_eps")
        self.set_eps.setPlaceholderText(_translate("MainWindow", "0.001"))

        self.image_dir_inp = QtWidgets.QLineEdit(menu)
        self.image_dir_inp.setGeometry(QtCore.QRect(410, 310, 431, 25))
        self.image_dir_inp.setObjectName("image_dir_inp")
    
    def _init_combo_boxes(self, 
                          menu: QtWidgets.QWidget, 
                          _translate: QtCore.QCoreApplication.translate) -> None:
        """
        Initializing combo boxes in settings menu.
        :param menu: tab menu -> settings menu.
        :param _translate: translator.
        :return: None
        """
        self.image_fmt = QtWidgets.QComboBox(menu)
        self.image_fmt.setGeometry(QtCore.QRect(570, 425, 80, 25))
        self.image_fmt.setObjectName("image_fmt")
        self.image_fmt.addItem("")
        self.image_fmt.addItem("")
        self.image_fmt.setItemText(0, _translate("MainWindow", "PNG"))
        self.image_fmt.setItemText(1, _translate("MainWindow", "JPEG"))

    def _init_btns(self,
                   menu: QtWidgets.QWidget,
                   _translate: QtCore.QCoreApplication.translate) -> None:
        """
        Initializing buttons in settings menu.
        :param menu: tab menu -> settings menu
        :param _translate: translator
        :return: None
        """
        self.set_default_settings_btn = QtWidgets.QPushButton(menu)
        self.set_default_settings_btn.setGeometry(QtCore.QRect(10, 710, 201, 28))
        self.set_default_settings_btn.setObjectName("set_default_settings_btn")
        self.set_default_settings_btn.setText(_translate("MainWindow", "Настройки по умолчанию"))

        self.set_settings_btn = QtWidgets.QPushButton(menu)
        self.set_settings_btn.setGeometry(QtCore.QRect(860, 710, 131, 28))
        self.set_settings_btn.setObjectName("set_settings_btn")
        self.set_settings_btn.setText(_translate("MainWindow", "Применить"))

        self.directory_finder_image = QtWidgets.QToolButton(menu)
        self.directory_finder_image.setGeometry(QtCore.QRect(850, 310, 30, 25))
        self.directory_finder_image.setObjectName("directory_finder_image")
        self.directory_finder_image.setText(_translate("MainWindow", "..."))

        self.directory_finder_file = QtWidgets.QToolButton(menu)
        self.directory_finder_file.setGeometry(QtCore.QRect(850, 380, 30, 25))
        self.directory_finder_file.setObjectName("directory_finder_file")
        self.directory_finder_file.setText(_translate("MainWindow", "..."))

    def dir_find(self, input_line: QtWidgets.QLineEdit) -> None:
        """
        method that interacts with the easygui module.
        Enables the ability to get the desired path to the data storage directory from the user.
        :param input_line: Path output field
        :return: None
        """
        path = easygui.diropenbox('Выберите папку')
        if self.create_image_directory.isChecked() and path:
            path += '\\Solution'
            input_line.setText(path)
            del path
            return None
        if path:
            input_line.setText(path)
            del path
            return None

    def _load_settings(self) -> None:
        """
        Uploading data from the settings file.json when initializing the settings window.
        Passes the values saved by the user when the program was last started to widgets.
        :return: None
        """
        with open(SETTING_PATH, 'r', encoding='utf-8') as file:
            setting = js.load(file)
        self.create_q.setChecked(setting['create_q'])
        self.create_m.setChecked(setting['create_m'])
        self.create_v.setChecked(setting['create_v'])
        self.create_phi.setChecked(setting['create_phi'])
        self.singular_point.setChecked(setting['singular_point'])
        self.show_extr.setChecked(setting['show_extr'])
        self.find_user_points.setChecked(setting['find_user_points'])
        self.set_eps.setText(setting['set_eps'])
        self.out_file.setChecked(setting['out_file'])
        self.out_GUI.setChecked(setting['out_GUI'])
        self.create_graphics.setChecked(setting['create_graphics'])
        self.create_image_directory.setChecked(setting['create_image_directory'])
        self.image_dir_inp.setText(setting['image_dir_inp'])
        self.file_directory_inp.setText(setting['file_dir_inp'])
        del setting
        del file

    def _set_default_settings(self) -> None:
        """
        Sets the default values accepted by the developer in all fields in the settings menu.
        :return: None
        """
        self.create_q.setChecked(True)
        self.create_m.setChecked(True)
        self.create_phi.setChecked(True)
        self.create_v.setChecked(True)
        self.singular_point.setChecked(False)
        self.show_extr.setChecked(False)
        self.find_user_points.setChecked(False)
        self.set_eps.setText('0.001')
        self.out_file.setChecked(True)
        self.out_GUI.setChecked(True)
        self.create_graphics.setChecked(True)
        self.create_image_directory.setChecked(True)
        image_dir_path = str(os.getcwd()).replace('\\scbv2', '') + '\\' + 'Solution'
        self.image_dir_inp.setText(image_dir_path)
        file_dir_path = str(os.getcwd()).replace('\\scbv2', '') + '\\' + 'Solution'
        self.file_directory_inp.setText(file_dir_path)
        del image_dir_path
        del file_dir_path
        # Save settings.
        self._set_settings()

    def _set_settings(self) -> None:
        """
        Checking the correctness of the settings entered by the user
        and then uploading them to a JSON file.
        :return: None
        """
        def check_eps(value: str) -> ((float or None), bool):
            """
            Checks whether the entered calculation accuracy value is correct.
            :param value:
            :return:
            """
            if value != '':
                try:
                    normal = float(value)
                    if normal > 0:
                        return float(value), True
                    return None, False
                except ValueError:
                    return None, False
            return None, True

        # Checking whether the calculation accuracy value is correct.
        # The second value is a flag that allows you to continue executing
        # the method logic with the correct value.
        eps, flg_eps = check_eps(self.set_eps.text())

        # When an empty value is returned it assigns the eps default value.
        if eps is None:
            eps = 0.001

        # If the value of the save directories is empty, it assigns default values.
        if self.image_dir_inp.text() == '':
            image_dir = str(os.getcwd())
        else:
            image_dir = self.image_dir_inp.text()

        if self.file_directory_inp.text() == '':
            file_directory = str(os.getcwd())
        else:
            file_directory = self.file_directory_inp.text()

        if flg_eps:
            settings_dict = {
                'create_q': self.create_q.isChecked(),
                'create_m': self.create_m.isChecked(),
                'create_phi': self.create_phi.isChecked(),
                'create_v': self.create_v.isChecked(),
                'singular_point': self.singular_point.isChecked(),
                'show_extr': self.show_extr.isChecked(),
                'find_user_points': self.find_user_points.isChecked(),
                'set_eps': str(eps),
                'out_file': self.out_file.isChecked(),
                'out_GUI': self.out_GUI.isChecked(),
                'create_graphics': self.create_graphics.isChecked(),
                'create_image_directory': self.create_image_directory.isChecked(),
                'image_dir_inp': image_dir,
                'file_dir_inp': file_directory
            }
            with open(SETTING_PATH, 'w', encoding='utf-8') as file:
                js.dump(settings_dict, file)
            del settings_dict, file
            del eps
            del flg_eps
            del file_directory
            del image_dir

    def get_settings(self) -> dict:
        """
        Returns a dictionary with the values of the settings.
        :return: Dictionary with the values of the settings.
        """
        return {
            "CREATE_Q": self.create_q.isChecked(),
            "CREATE_M": self.create_m.isChecked(),
            "CREATE_PHI": self.create_phi.isChecked(),
            "CREATE_V": self.create_v.isChecked(),
            "SINGULAR_POINTS": self.singular_point.isChecked(),
            "SHOW_EXTR": self.show_extr.isChecked(),
            "USER_POINTS": self.find_user_points.isChecked(),
            "OUT_FILE": self.out_file.isChecked(),
            "OUT_GUI": self.out_GUI.isChecked(),
            "CREATE_GRAPHICS": self.create_graphics.isChecked(),
            "IMAGE_DIR": self.image_dir_inp.text(),
            "FILE_DIR": self.file_directory_inp.text(),
            "IMAGE_FMT": self.image_fmt.currentText(),
            "EPS": float(self.set_eps.text())
        }
