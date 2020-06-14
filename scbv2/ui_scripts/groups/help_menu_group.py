# -*- coding: utf-8 -*-
# You are using an open source project
# Date when the first version of this module was created: 14.06.2020 10:22 AM
# Date when the module was last edited: 09.06.2020 1:00 AM
# The Creator is not responsible for any changes made by a third party developer
# Author: Biro Ilya. St.Tell MAIL:st.tell@mail.ru Russia, Moscow

from PyQt5 import QtCore, QtWidgets, QtGui


class HelpMenu(object):
    def __init__(self, menu: QtWidgets.QWidget):
        self.help_window = QtWidgets.QTextBrowser(menu)
        self.help_window.setGeometry(QtCore.QRect(50, 50, 900, 650))
        self.help_window.setObjectName('out_window')
        text = self._get_text()
        self.help_window.setText(text)
        self.help_window.setFont(QtGui.QFont("monospace", 11))
        self.help_window.setOpenExternalLinks(True)

    @staticmethod
    def _get_text():
        text = '-' * 144
        text += '<h3><span style=\" color: #1b2f6e;\">' + \
                '<font face="Verdana">Добро пожаловать! SoM v.1.0.3</font></span></h3>'
        text += '-' * 144
        text += '''<h4><span style=\" color: #0d2266;\">
<font face="Verdana">Инструкция по использованию Менеджера решений</font></span></h4>
<h5><span style=\" color: #383838; font-size:medium\"><font face="monospace">
<p>Программа предназначена для вычисисления исключительно задач на поперечный изгиб бесшарнирного, 
статически определимого стержня.
<p style="margin-left: 50px;">Чтобы получить решение своей задачи нужно провести следующие операции:</p>
</font>
<font face="monospace">
<p>1. Укажите длину балки и метрику этой длины(Рекомендуется задавать метрику в системе СИ, метры)</p>
<p>2. Параметры "Модуль упругости(E)" и "Момент инерции сечения(J)" нужны для вычисления прогибов в
конкретных материалах и формах балки. По умолчанию они равны 1,
что исключает влияние материала и формы сечения на результат вычислений.</p>
<p>3. Выберите тип закрепления балки. На данный момент доступны 2 вида:</p>
<p style="margin-left: 50px;">1) Шарнирно-опертая. 2 шарнира в разных точках.</p>
<p style="margin-left: 50px;">2) Заделка. Заделка препятствует перемещению по всем осям и 
сводит момент к нулю в закреплении.</p>
<p>4. Добавьте координаты точек опорных реакций в зависимости от того какой тип закрепления выбран.</p>
<p style="margin-left: 50px;">Для Шарнирно-опертой балки: 2 опоры в разных точках балки.</p>
<p style="margin-left: 50px;">Для Заделки: Одна опора в точке х=0 м.</p>
<p>5. Добавьте требуемые нагрузки.</p>
<p style="margin-left: 25px;">Подробнее:</p>
<p style="margin-left: 50px;">При добавлении нагрузок направление указывается с помощью 
отрицательного или положительного значения.</p>
<p style="margin-left: 50px;">Положительное значение нагрузки задает направление вниз (Для момента влево)</p>
<p style="margin-left: 50px;">Отрицательное значение нагрузки задает направление вверх (Для момента вправо)</p>
<p>6. Убедитесь в верности постановки задачи и приступите к решению.</p>
</font></h5></span>
'''
        text += '-' * 144
        text += '''
<h4><span style=\" color: #0d2266;\">
<font face="Verdana">Сообщить об ошибке.</font></span></h4>
<h5><span style=\" color: #383838;\"><font face="Verdana">Сообщить об ошибке можно по указанной почте:
<a href="mailto:st.tell@mail.ru">st.tell@mail.ru</a>
</span></h5>
        '''
        text += '-' * 144
        return text
