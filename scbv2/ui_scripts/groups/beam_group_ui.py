# -*- coding: utf-8 -*-
# You are using an open source project
# Date when the first version of this module was created: 05.06.2020 7:00 AM
# Date when the module was last edited: 09.06.2020 1:00 AM
# The Creator is not responsible for any changes made by a third party developer
# Author: Biro Ilya. St.Tell MAIL:st.tell@mail.ru Russia, Moscow

from PyQt5 import QtCore, QtWidgets


class BeamGroup(object):
    # The class initializes a field for entering beam parameters.
    def __init__(self,
                 menu: QtWidgets.QWidget):
        _translate = QtCore.QCoreApplication.translate
        self._init_input_boxes(menu, _translate)
        self._init_labels(menu, _translate)
        self._init_combo_boxes(menu, _translate)
        # Default support type
        self.reaction_type = "Шарнирно-опертая (Два шарнира)"

    def _init_input_boxes(self,
                          menu: QtWidgets.QWidget,
                          _translate: QtCore.QCoreApplication.translate):
        """
        Initializes Input boxes
        :param menu: Solver menu
        :param _translate: Translator
        :return: None
        """
        self.beam_length_inp = QtWidgets.QLineEdit(menu)
        self.beam_length_inp.setGeometry(QtCore.QRect(105, 45, 50, 25))
        self.beam_length_inp.setObjectName("beam_length_inp")

        self.elastic_modules_inp = QtWidgets.QLineEdit(menu)
        self.elastic_modules_inp.setGeometry(QtCore.QRect(165, 80, 81, 25))
        self.elastic_modules_inp.setObjectName("elastic_modules_inp")
        self.elastic_modules_inp.setPlaceholderText(_translate("MainWindow", "1"))

        self.moment_inert_inp = QtWidgets.QLineEdit(menu)
        self.moment_inert_inp.setGeometry(QtCore.QRect(210, 112, 81, 25))
        self.moment_inert_inp.setObjectName("moment_inert_inp")
        self.moment_inert_inp.setPlaceholderText(_translate("MainWindow", "1"))

    def _init_labels(self,
                     menu: QtWidgets.QWidget,
                     _translate: QtCore.QCoreApplication.translate):
        """
        Initializes labels
        :param menu: Solver menu
        :param _translate: Translator
        :return: None
        """
        self._beam_params_lab = QtWidgets.QLabel(menu)
        self._beam_params_lab.setGeometry(QtCore.QRect(10, 10, 180, 20))
        self._beam_params_lab.setObjectName("_beam_params_lab")
        self._beam_params_lab.setText(_translate("MainWindow", "Параметры балки"))

        self._beam_length_lab = QtWidgets.QLabel(menu)
        self._beam_length_lab.setGeometry(QtCore.QRect(10, 45, 90, 25))
        self._beam_length_lab.setObjectName("_beam_length_lab")
        self._beam_length_lab.setText(_translate("MainWindow", "Длина балки:"))

        self._elastic_modules_lab = QtWidgets.QLabel(menu)
        self._elastic_modules_lab.setGeometry(QtCore.QRect(10, 80, 150, 25))
        self._elastic_modules_lab.setObjectName("_elastic_modules_lab")
        self._elastic_modules_lab.setText(_translate("MainWindow", "Модуль упругости(Е):"))

        self._elastic_modules_mtrc = QtWidgets.QLabel(menu)
        self._elastic_modules_mtrc.setGeometry(QtCore.QRect(250, 80, 55, 24))
        self._elastic_modules_mtrc.setObjectName("_elastic_modules_mtrc")
        self._elastic_modules_mtrc.setText(_translate("MainWindow", "МПа"))

        self._moment_inert_lab = QtWidgets.QLabel(menu)
        self._moment_inert_lab.setGeometry(QtCore.QRect(10, 112, 200, 25))
        self._moment_inert_lab.setObjectName("_moment_inert_lab")
        self._moment_inert_lab.setText(_translate("MainWindow", "Момент инерции сечения(J):"))

        self._moment_inert_mtrc = QtWidgets.QLabel(menu)
        self._moment_inert_mtrc.setGeometry(QtCore.QRect(295, 112, 55, 24))
        self._moment_inert_mtrc.setObjectName("_moment_inert_mtrc")
        self._moment_inert_mtrc.setText(_translate("MainWindow", "Cм^4"))

        self._suppor_type_lab = QtWidgets.QLabel(menu)
        self._suppor_type_lab.setGeometry(QtCore.QRect(10, 145, 181, 25))
        self._suppor_type_lab.setObjectName("_suppor_type_lab")
        self._suppor_type_lab.setText(_translate("MainWindow", "Комбинация типов опор:"))

    def _init_combo_boxes(self,
                          menu: QtWidgets.QWidget,
                          _translate: QtCore.QCoreApplication.translate):
        """
        Initializes labels
        :param menu: Solver menu
        :param _translate: Translator
        :return: None
        """
        self.support_type_inp = QtWidgets.QComboBox(menu)
        self.support_type_inp.setGeometry(QtCore.QRect(10, 170, 380, 25))
        self.support_type_inp.setObjectName("support_type_inp")
        self.support_type_inp.addItem("")
        self.support_type_inp.addItem("")
        self.support_type_inp.currentIndexChanged.connect(self._reset_reaction)

        self._beam_length_mtrc = QtWidgets.QComboBox(menu)
        self._beam_length_mtrc.setGeometry(QtCore.QRect(160, 45, 51, 25))
        self._beam_length_mtrc.setObjectName("_beam_length_mtrc")
        self._beam_length_mtrc.addItem("")
        self._beam_length_mtrc.addItem("")
        self._beam_length_mtrc.addItem("")
        self._beam_length_mtrc.addItem("")

        self._beam_length_mtrc.setItemText(0, _translate("MainWindow", "м"))
        self._beam_length_mtrc.setItemText(1, _translate("MainWindow", "мм"))
        self._beam_length_mtrc.setItemText(2, _translate("MainWindow", "см"))
        self._beam_length_mtrc.setItemText(3, _translate("MainWindow", "км"))

        self.support_type_inp.setItemText(0, _translate("MainWindow", "Шарнирно-опертая (Два шарнира)"))
        self.support_type_inp.setItemText(1, _translate("MainWindow", "Заделка с одного края"))

    def _reset_reaction(self) -> None:
        """
        Reloads the support type values selected by the user
        :return: None
        """
        self.reaction_type = self.support_type_inp.currentText()

    def return_values(self,
                      main_window: QtWidgets.QMainWindow) -> (float, float, float, str):
        """
        Method used by the compile class.
        Returns the values entered by the user and checks them for correctness.
        :param main_window: Main Window object.
        :return: length, elastic, moment of inertia, reaction_type
        """
        length = self.beam_length_inp.text()
        elastic = self.elastic_modules_inp.text()
        inertia_mom = self.moment_inert_inp.text()

        # Checking whether the beam length is correct
        try:
            if float(length.lstrip().rstrip().replace(',', '.')) != 0.0:
                if self._beam_length_mtrc.currentText() == 'м':
                    length = float(length.lstrip().rstrip().replace(',', '.'))
                elif self._beam_length_mtrc.currentText() == 'мм':
                    length = float(length.lstrip().rstrip().replace(',', '.')) / 1000
                elif self._beam_length_mtrc.currentText() == 'см':
                    length = float(length.lstrip().rstrip().replace(',', '.')) / 100
                elif self._beam_length_mtrc.currentText() == 'км':
                    length = float(length.lstrip().rstrip().replace(',', '.')) * 1000
            else:
                self.error_box(main_window,
                               'Длина балки не может быть нулевая.',
                               'Ошибка')
                return None, None, None, None
        except ValueError:
            self.error_box(main_window,
                           'Некорректная длина балки.',
                           'Ошибка')
            return None, None, None, None

        # Checking the correctness of the moment of inertia and modulus of elasticity
        try:
            if elastic.rstrip().lstrip().replace(',', '.') != '':
                elastic = float(elastic.rstrip().lstrip().replace(',', '.'))
            else:
                elastic = 1
        except ValueError:
            self.error_box(main_window,
                           'Некорректное значение модуля упругости.',
                           'Ошибка')
            return None, None, None, None
        try:
            if inertia_mom.rstrip().lstrip().replace(',', '.') != '':
                inertia_mom = float(inertia_mom.rstrip().lstrip().replace(',', '.'))
            else:
                inertia_mom = 1
        except ValueError:
            self.error_box(main_window,
                           'Некорректное значение модуля момента инерции сечения.',
                           'Ошибка')
            return None, None, None, None

        reaction_type = self.support_type_inp.currentText()
        return length, elastic, inertia_mom, reaction_type

    @staticmethod
    def error_box(main_window: QtWidgets.QWidget,
                  msg: str,
                  title: str) -> None:
        """
        Creating a pop-up error window.
        :param main_window: MainWindow object
        :param msg: message
        :param title: message title
        :return: None
        """
        QtWidgets.QMessageBox.critical(main_window, title, msg)
