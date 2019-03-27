# -*- coding: utf-8 -*-
# @Time    : 19-3-26 下午5:45
# @Author  : YanPengliang
# @Project : myMail
# @File    : NewEmail.py
# @Version : v1.0

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from MyButton import *
from MenuWindow import *
from MenuBar import *


class NewEmail(QWidget):
    def __init__(self, *args, parent=None):
        super().__init__(parent)
        self.setWindowTitle("新邮件")
        self.resize(760, 700)
        self.move(300, 50)
        self.menu = MenuBar(self)
        self.setFont(QFont("ubuntu", 11))  ##设置字体

        self.name_label = QLabel('收件人:', self)
        self.name_label.move(20, 50)
        self.name_input = QLineEdit("", self)
        self.name_input.move(80, 50)
        self.name_input.resize(500,25)

        self.subject_label = QLabel('主     题:', self)
        self.subject_label.move(20, 100)
        self.subject_input = QLineEdit("", self)
        self.subject_input.move(80, 100)
        self.subject_input.resize(500, 25)

        self.passage_label = QLabel("正     文:", self)
        self.passage_label.move(20, 150)
        self.passage_input=QTextEdit("",self)
        self.passage_input.resize(self.width()-120,self.height()-150)
        self.passage_input.move(80,150)


if __name__ == '__main__':
    import cgitb

    cgitb.enable(format='text')
    a = QApplication(sys.argv)
    m = NewEmail()
    m.show()
    sys.exit(a.exec_())
