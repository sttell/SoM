# -*- coding: utf-8 -*-
# You are using an open source project
# Date when the first version of this module was created: 05.06.2020 7:00 AM
# Date when the module was last edited: 09.06.2020 00:51 AM
# The Creator is not responsible for any changes made by a third party developer
# Author: Biro Ilya. St.Tell MAIL:st.tell@mail.ru Russia, Moscow

from PyQt5 import QtWidgets, QtCore, QtGui


class DecoreElements(object):
    # A class that creates decorative objects in the main window.
    def __init__(self,
                 menu: QtWidgets.QWidget):
        self.decor_line_V = QtWidgets.QFrame(menu)
        self.decor_line_V.setGeometry(QtCore.QRect(400, -2, 3, 750))
        self.decor_line_V.setFrameShape(QtWidgets.QFrame.VLine)
        self.decor_line_V.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.decor_line_V.setObjectName("decor_line_V")

        self.decor_line_H_1 = QtWidgets.QFrame(menu)
        self.decor_line_H_1.setGeometry(QtCore.QRect(0, 35, 400, 3))
        self.decor_line_H_1.setFrameShape(QtWidgets.QFrame.HLine)
        self.decor_line_H_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.decor_line_H_1.setObjectName("decor_line_H_1")

        self.decor_line_H_2 = QtWidgets.QFrame(menu)
        self.decor_line_H_2.setGeometry(QtCore.QRect(0, 210, 400, 3))
        self.decor_line_H_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.decor_line_H_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.decor_line_H_2.setObjectName("decor_line_H_2")

        self.decor_line_H_3 = QtWidgets.QFrame(menu)
        self.decor_line_H_3.setGeometry(QtCore.QRect(0, 240, 400, 3))
        self.decor_line_H_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.decor_line_H_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.decor_line_H_3.setObjectName("decor_line_H_3")

        self.decor_line_H_4 = QtWidgets.QFrame(menu)
        self.decor_line_H_4.setGeometry(QtCore.QRect(0, 670, 400, 3))
        self.decor_line_H_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.decor_line_H_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.decor_line_H_4.setObjectName("decor_line_H_4")

    def set_task_label(self,
                       centralwidget: QtWidgets.QWidget,
                       task_type: str) -> None:
        """
        The method creates a Label in the upper-right field of the window.
        :param centralwidget: The Central widget where the Label will be created.
        :param task_type: String value of the task type.
        :return: None
        """
        _translate = QtCore.QCoreApplication.translate
        self.solver_label = QtWidgets.QLabel(centralwidget)
        self.solver_label.setGeometry(QtCore.QRect(520, 5, 320, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.solver_label.setFont(font)
        self.solver_label.setObjectName("solver_label")
        self.solver_label.setText(_translate("MainWindow", task_type))
