# -*- coding: utf-8 -*-
# You are using an open source project
# Date when the first version of this module was created: 04.06.2020 7:00 AM
# Date when the module was last edited: 04.06.2020 7:00 AM
# The Creator is not responsible for any changes made by a third party developer
# Author: Biro Ilya. St.Tell MAIL:st.tell@mail.ru Russia, Moscow
import local.local_var_EN as EnLoc
import local.local_var_RUS as RusLoc
import task_type_selection_menu
import scbv2.main_window
import ss.msg_v110
import torsion.msg_v120
import sys

if __name__ == '__main__':
    # Launch the task type selection menu.
    # Returns the task type.
    type_task = task_type_selection_menu.run()
    if type_task is not None:
        # If the task type is statically definable.
        # Search for deflection from transverse loads.
        if type_task in [EnLoc.tt_cross_bend_stc, RusLoc.tt_cross_bend_stc]:
            sol_code = scbv2.main_window.run_task()
            print(f'Programm exit with code: {sol_code}')
        # If the task type is Statically definable
        # Search for elongation or compression under longitudinal loads.
        elif type_task in [EnLoc.tt_sec_select, RusLoc.tt_sec_select]:
            sol_code = ss.msg_v110.run_task()
        # If the issue type is Torsion.
        elif type_task in [EnLoc.tt_torsion, RusLoc.tt_torsion]:
            sol_code = torsion.msg_v120.run_task()
    else:
        del type_task
        sys.exit()
