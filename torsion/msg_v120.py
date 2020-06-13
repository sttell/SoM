# -*- coding: utf-8 -*-
# You are using an open source project
# Date when the first version of this module was created: 04.06.2020 7:00 AM
# Date when the module was last edited: 13.06.2020 6:56 AM
# The Creator is not responsible for any changes made by a third party developer
# Author: Biro Ilya. St.Tell MAIL:st.tell@mail.ru Russia, Moscow

from PyQt5 import QtCore, QtGui, QtWidgets


class UIDialog(object):
    def __init__(self):
        dialog = QtWidgets.QDialog()
        self._setup_ui(dialog)
        self._retranslate_ui(dialog)
        
    def _setup_ui(self, dialog):
        dialog.setObjectName("Dialog")
        dialog.resize(400, 145)
        self.buttonBox = QtWidgets.QDialogButtonBox(dialog)
        self.buttonBox.setGeometry(QtCore.QRect(40, 100, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(dialog)
        self.label.setGeometry(QtCore.QRect(50, 50, 301, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self._retranslate_ui(dialog)
        self.buttonBox.accepted.connect(dialog.accept)
        self.buttonBox.rejected.connect(dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def _retranslate_ui(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("Dialog", "Error. Not release"))
        self.label.setText(_translate("Dialog", "Please, wait release SOM version 1.2.0"))
        dialog.show()


def run_task():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = UIDialog()
    sys.exit(app.exec_())
