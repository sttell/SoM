# -*- coding: utf-8 -*-
# You are using an open source project
# Date when the first version of this module was created: 04.06.2020 7:00 AM
# Date when the module was last edited: 04.06.2020 7:00 AM
# The Creator is not responsible for any changes made by a third party developer
# Author: Biro Ilya. St.Tell MAIL:st.tell@mail.ru Russia, Moscow

from PyQt5 import QtCore, QtGui, QtWidgets


class Mark(object):
    """
    The main class responsible
    for creating the main application window
    and marking fields for objects from child classes.
    """
    def __init__(self,
                 centralwidget: QtWidgets.QWidget) -> (QtWidgets.QWidget,
                                                       QtWidgets.QWidget,
                                                       QtWidgets.QLayout,
                                                       QtWidgets.QLayout):
        """
        Method for initializing fields and the main window object.
        :return: None
        """

        # Main TabMenu
        self.tab_menu = QtWidgets.QTabWidget(centralwidget)
        self.tab_menu.setGeometry(QtCore.QRect(0, 0, 1000, 800))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tab_menu.setFont(font)
        self.tab_menu.setObjectName("tab_menu")
        # Item in tab menu: solver menu
        self.solver_menu = QtWidgets.QWidget()
        self.solver_menu.setObjectName("solver_menu")
        self.tab_menu.addTab(self.solver_menu, "Запуск решения")

        # Item in tab menu: settings
        self.settings_menu = QtWidgets.QWidget()
        self.settings_menu.setObjectName("settings_menu")
        self.tab_menu.addTab(self.settings_menu, "Настройки")

        # Item in tab menu: help
        self.help_menu = QtWidgets.QWidget()
        self.help_menu.setObjectName("help_menu")
        self.tab_menu.addTab(self.help_menu, "Помощь")

        # Left Layout in settings menu.
        # Contain CheckBoxes for settings solver
        self.verticalLayoutWidget = QtWidgets.QWidget(self.settings_menu)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 60, 361, 371))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        # Right Layout in settings menu.
        # Contain CheckBoxes for settings solver
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.settings_menu)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(410, 60, 393, 211))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
