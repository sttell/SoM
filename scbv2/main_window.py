# -*- coding: utf-8 -*-
# You are using an open source project
# Date when the first version of this module was created: 04.06.2020 7:00 AM
# Date when the module was last edited: 09.06.2020 00:23 PM
# The Creator is not responsible for any changes made by a third party developer
# Author: Biro Ilya. St.Tell MAIL:st.tell@mail.ru Russia, Moscow

from PyQt5 import QtCore, QtWidgets, Qt
import scbv2.ui_scripts.groups.add_load_group_ui as load_group
import scbv2.ui_scripts.widgets.window_markings as marks
import scbv2.ui_scripts.groups.beam_group_ui as beam_group
import scbv2.ui_scripts.groups.output_group as out_group
import scbv2.ui_scripts.groups.decore_group as dec_group
import scbv2.ui_scripts.groups.help_menu_group as hlp
import scbv2.ui_scripts.groups.setting_menu as sttng
import scbv2.ui_scripts.compiler as compil
import scbv2.solver as solver


class UiMainWindow(Qt.QWidget):

    def setup_ui(self):
        # Initializing the main window object
        self.MainWindow = QtWidgets.QMainWindow()
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(1000, 801)
        # Central widget init
        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Marking group
        marking = marks.Mark(self.centralwidget)
        # Beam Group Menu
        bg = beam_group.BeamGroup(marking.solver_menu)
        # Load Group Menu
        lgm = load_group.AddLoadGroup(marking.solver_menu, self.MainWindow)
        # Output Group Menu
        og = out_group.OutGroup(marking.solver_menu)
        # Decoreation Group Menu
        dec = dec_group.DecoreElements(marking.solver_menu)
        # Compiler btn
        comp = compil.Compiler(marking.solver_menu)
        # Settings
        settings = sttng.SettingMenu(marking.settings_menu,
                                     [marking.verticalLayoutWidget, marking.verticalLayoutWidget_2],
                                     {marking.verticalLayoutWidget: marking.verticalLayout,
                                      marking.verticalLayoutWidget_2: marking.verticalLayout_2})
        # Help menu
        help_menu = hlp.HelpMenu(marking.help_menu)
        comp.start_sol_btn.clicked.connect(
                lambda obj,
                beam=bg,
                load=lgm,
                main_wind=self.MainWindow: self.start_compile(comp,
                                                              beam,
                                                              load,
                                                              settings,
                                                              main_wind,
                                                              og.out_window,
                                                              og.pbar))
        dec.set_task_label(self.centralwidget, "Поперечный изгиб (Статически определимая)")
        self._st_mb_init(marking)
        self._retrans_marks_ui(self.MainWindow)

    @staticmethod
    def start_compile(obj: compil.Compiler,
                      obj1: beam_group.BeamGroup,
                      obj2: load_group.AddLoadGroup,
                      obj3: sttng.SettingMenu,
                      main_window: QtWidgets.QMainWindow,
                      out_window: QtWidgets.QTextBrowser,
                      pbar: QtWidgets.QProgressBar):
        """
        Static method. Accepts objects containing the parameters
        needed to run the solution and passes them to the solver.
        :param obj: The object of the compilers of the data.
        :param obj1: The object contains the parameters of the beam.
        :param obj2: An object containing loads and supports.
        :param obj3: Menu object with settings.
        :param main_window: The object of the main window.
        :param out_window: Object of the data output window.
        :param pbar: Progress Bar.
        :return: Nothing.
        """
        # The collection of parameters of the problem.
        # At the output, we have a dictionary with the data of the problem statement.
        task_dict = obj.compile_data(obj1, obj2, main_window)
        # The collection of settings.
        # At the output, we have a dictionary with data about settings.
        setting_dict = obj3.get_settings()
        # If data is entered incorrectly, an error may occur,
        # which will be intercepted by the method of object 3.
        # In this case, the value None will be returned to the task_dict variable.
        # In order not to continue running the program, the following construction is intended.
        if task_dict is not None:
            sol = solver.Solver(out_window, pbar)
            sol.run_solver(task_dict, setting_dict)

    def _st_mb_init(self, mark: marks.Mark) -> None:
        """
        Final loading of the main window.
        :param mark: Marking object.
        :return: Nothing
        """
        self.MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(self.MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 26))
        self.menubar.setObjectName("menubar")
        self.MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(self.MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.MainWindow.setStatusBar(self.statusbar)

        mark.tab_menu.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)
        self.MainWindow.show()

    @staticmethod
    def _retrans_marks_ui(main_window: QtWidgets.QMainWindow) -> None:
        """
        Retranslate UI method.
        Sets the title of the main program window
        :param main_window: MainWindow object
        :return: None
        """
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("MainWindow", "SOM v.1.0.3 - Поперечный изгиб (Статически определимая)"))


def run_task():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = UiMainWindow()
    ui.setup_ui()
    app.exec_()
    return 0
