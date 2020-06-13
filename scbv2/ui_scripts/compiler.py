# -*- coding: utf-8 -*-
# You are using an open source project
# Date when the first version of this module was created: 04.06.2020 7:00 AM
# Date when the module was last edited: 04.06.2020 00:15 AM
# The Creator is not responsible for any changes made by a third party developer
# Author: Biro Ilya. St.Tell MAIL:st.tell@mail.ru Russia, Moscow

from PyQt5 import QtWidgets, QtCore
from scbv2.ui_scripts.groups.add_load_group_ui import AddLoadGroup
from scbv2.ui_scripts.groups.beam_group_ui import BeamGroup


class Compiler(object):
    # A class used for collecting data from passed objects.
    def __init__(self, menu: QtWidgets.QWidget):
        # Translator of the Start button text
        _translate = QtCore.QCoreApplication.translate
        # Creating a button in the task parameters entry menu.
        self.start_sol_btn = QtWidgets.QPushButton(menu)
        self.start_sol_btn.setGeometry(QtCore.QRect(70, 690, 241, 41))
        self.start_sol_btn.setObjectName("start_sol_btn")
        self.start_sol_btn.setText(_translate("MainWindow", "Начать"))

    @staticmethod
    def compile_data(bg: BeamGroup,
                     alg: AddLoadGroup,
                     main_window: QtWidgets.QWidget) -> (dict or None):
        """
        Data collection method
        :param bg: beam group object
        :param alg: add load group object
        :param main_window: main window object
        :return: Dictionary with data about the problem statement.
        """
        lenght, elastic, inertion_mom, reac_type = bg.return_values(main_window)
        if None in (lenght, elastic, inertion_mom, reac_type):
            return None
        force_list, reac_list, hinghle_list = alg.get_data()
        if len(force_list) == 0:
            pass
        if reac_type == "Шарнирно-опертая (Два шарнира)" and len(reac_list) != 2:
            print(reac_list)
            bg.error_box(main_window, 'Некорректная постановка задачи. Измените реакции или тип опоры.', 'Ошибка')
            return None
        if reac_type == "Заделка с одной стороны" and (reac_list[0] != 0 or len(reac_list) != 1):
            bg.error_box(main_window, 'Некорректная постановка задачи. Измените реакции или тип опоры.', 'Ошибка')
            return None
        return {"FORCES": force_list,
                "REACTIONS": reac_list,
                "HINGHLES": hinghle_list,
                "BEAM_LENGHT": lenght,
                "ELASTIC_MODULE": elastic,
                "INERTION_MOMENT": inertion_mom,
                "REACTION_TYPE": reac_type}
