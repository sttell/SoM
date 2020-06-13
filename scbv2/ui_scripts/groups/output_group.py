# -*- coding: utf-8 -*-
# You are using an open source project
# Date when the first version of this module was created: 05.06.2020 7:00 AM
# Date when the module was last edited: 09.06.2020 00:48 AM
# The Creator is not responsible for any changes made by a third party developer
# Author: Biro Ilya. St.Tell MAIL:st.tell@mail.ru Russia, Moscow

from PyQt5 import QtWidgets, QtCore


class OutGroup(object):
    # Class containing the logic of the output window object

    def __init__(self,
                 menu: QtWidgets.QWidget):
        self.out_window = QtWidgets.QTextBrowser(menu)
        self.out_window.setGeometry(QtCore.QRect(408, 4, 580, 701))
        self.out_window.setObjectName('out_window')

    def add_result(self, text: str) -> None:
        """
        Outputs the passed text to the output window.
        :param text: text
        :return: None
        """
        self.out_window.setText(text)
