# -*- coding: utf-8 -*-
# You are using an open source project
# Date when the first version of this module was created: 04.06.2020 7:00 AM
# Date when the module was last edited: 13.06.2020 6:52 AM
# The Creator is not responsible for any changes made by a third party developer
# Author: Biro Ilya. St.Tell MAIL:st.tell@mail.ru Russia, Moscow

# import PyQt5, sys modules
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
import sys

# Reading a file with the specified interface localization settings
set_loc_file = open('local_setting.txt', 'r')
setting_loc = set_loc_file.readline()
set_loc_file.close()
# Applying interface localization settings and import modules
if setting_loc == 'RUS':
    import local.local_var_RUS as Loc
elif setting_loc == 'EN':
    import local.local_var_EN as Loc


def find_lib_path():
    """
    Finding the way to connect plugins for PyQt5 to work correctly
    :return: PATH to plugin directory
    """
    return '\\'.join(sys.argv[0].split('/')[:-1]) + '\\Lib\\site-packages\\PyQt5\\Qt\\plugins'


# Setting the path to PyQt5 plugins
LIB_PATH = find_lib_path()
Qt.QApplication.addLibraryPath(LIB_PATH)
QtCore.QCoreApplication.addLibraryPath(LIB_PATH)

del LIB_PATH
del set_loc_file


class UIMainWindow(object):
    def __init__(self, app, mw):
        """
        Initializing the start window object
        :param app: Application object
        :param mw: Main Window object
        """
        # An argument containing the default task type
        self.TASK_TYPE = None
        # Argumet - application object
        self.app = app
        # Arg - main_window object
        self.mw = mw
        # User localisation interface
        self.LOCALE = setting_loc
        self._setup_ui()

    def _setup_ui(self, main_window):
        # Init main_window
        main_window.setObjectName("main_window")
        main_window.resize(700, 400)

        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")

        # Label user greetings
        self.greeting_lab = QtWidgets.QLabel(self.centralwidget)
        self.greeting_lab.setEnabled(True)
        self.greeting_lab.setGeometry(QtCore.QRect(150, 10, 390, 50))
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.greeting_lab.size_policy().hasHeightForWidth())
        self.greeting_lab.setSizePolicy(size_policy)
        # Font settings for this label
        font = QtGui.QFont()
        # Font size
        font.setPointSize(15)
        self.greeting_lab.setFont(font)
        self.greeting_lab.setObjectName("greeting_lab")

        # Button responsible for closing the window and passing the user selected argument
        self.start_btn = QtWidgets.QPushButton(self.centralwidget)
        self.start_btn.setGeometry(QtCore.QRect(230, 250, 250, 50))
        # Font settings for this label
        font = QtGui.QFont()
        # Font size
        font.setPointSize(12)
        self.start_btn.setFont(font)
        self.start_btn.setObjectName("start_btn")
        # Tracking the button click event. The method is being executed _clicked_btn
        self.start_btn.clicked.connect(self._clicked_btn)

        # Command Box for selecting the type of problem to solve
        self.task_type_cb = QtWidgets.QComboBox(self.centralwidget)
        self.task_type_cb.setGeometry(QtCore.QRect(130, 140, 430, 40))
        font = QtGui.QFont()
        # Font settings
        font.setFamily("Microsoft JhengHei")
        # Font size
        font.setPointSize(10)
        self.task_type_cb.setFont(font)
        self.task_type_cb.setObjectName("task_type_cb")
        self.task_type_cb.addItem("")
        self.task_type_cb.addItem("")
        self.task_type_cb.addItem("")
        # Event tracking changing the task type parameter by the user.
        # The method is being executed _clicked_cb
        self.task_type_cb.currentIndexChanged.connect(self._clicked_cb)

        # Responsible for changing localization settings by the user
        self.set_local = QtWidgets.QComboBox(self.centralwidget)
        self.set_local.setGeometry(QtCore.QRect(620, 20, 70, 30))
        # Font settings
        font.setFamily("Microsoft JhengHei")
        # Font size
        font.setPointSize(9)
        self.set_local.setFont(font)
        self.set_local.setObjectName("set_local")
        self.set_local.addItem("")
        self.set_local.addItem("")
        # Event tracking user change of localization settings selection
        # The method is being executed _reset_local
        self.set_local.currentIndexChanged.connect(self._reset_local)

        # Label located on the combobox to select the type of task
        self.type_task_lab = QtWidgets.QLabel(self.centralwidget)
        self.type_task_lab.setGeometry(QtCore.QRect(130, 90, 441, 41))
        # Font settings
        font = QtGui.QFont()
        # Font size
        font.setPointSize(12)
        self.type_task_lab.setFont(font)
        self.type_task_lab.setObjectName("type_task_lab")

        main_window.setCentralWidget(self.centralwidget)

        # Menubar init
        self.menubar = QtWidgets.QMenuBar(main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 25))
        self.menubar.setObjectName("menubar")
        main_window.setMenuBar(self.menubar)

        # Statusbar init
        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)

        self.retranslate_ui(main_window)

        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslate_ui(self, main_window):
        # Translate object
        _translate = QtCore.QCoreApplication.translate

        # Main Window title
        main_window.setWindowTitle(_translate("main_window", Loc.main_window_label))

        # The names are taken from variables in the imported module
        # depending on the user's chosen interface localization

        # Label titles
        self.greeting_lab.setText(_translate("main_window", Loc.welcome_to_SOM))
        self.start_btn.setText(_translate("main_window", Loc.start))
        self.task_type_cb.setItemText(0, _translate("main_window", Loc.tt_cross_bend_stc))
        self.task_type_cb.setItemText(1, _translate("main_window", Loc.tt_torsion))
        self.task_type_cb.setItemText(2, _translate("main_window", Loc.tt_sec_select))
        self.type_task_lab.setText(_translate("main_window", Loc.sel_type_lab))

        if self.LOCALE == 'RUS':
            self.set_local.setItemText(0, _translate("main_window", Loc.set_loc_ru))
            self.set_local.setItemText(1, _translate("main_window", Loc.set_loc_en))
        else:
            self.set_local.setItemText(0, _translate("main_window", Loc.set_loc_en))
            self.set_local.setItemText(1, _translate("main_window", Loc.set_loc_ru))

    def _clicked_cb(self):
        """
        Action when the user selects a new value in CommandBox.
        Changes the attribute parameter TASK_TYPE.
        :return: NONE
        """
        self.TASK_TYPE = self.task_type_cb.currentText()

    def _clicked_btn(self):
        """
        Actions performed when the start button is clicked.
        Closes the task type selection window.
        :return: NONE
        """
        self.mw.close()
        self.app.exec_()
        self.TASK_TYPE = self.task_type_cb.currentText()

    def _reset_local(self):
        """
        Changing localization parameters.
        Overwrites information to the settings file.
        To apply the parameters, the window must be restarted.
        :return: NONE
        """
        new_local = self.set_local.currentText()
        self.LOCALE = self.set_local.currentText()
        file = open('local_setting.txt', 'w')
        file.write(new_local)
        file.close()


def run():
    """
    This function is responsible for creating a window
    and further using the widget by the user.
    Output data: type of problem to solve
    :return: task type
    """
    import sys

    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = UIMainWindow(app, main_window)
    main_window.show()
    app.exec_()

    # User task type
    tt = ui.TASK_TYPE

    # Clear variable
    global setting_loc
    del setting_loc
    del ui
    del app
    del main_window

    return tt
