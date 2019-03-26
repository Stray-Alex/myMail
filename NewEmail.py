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
    def __init__(self,*args,parent=None):
        super().__init__(parent)
        self.setWindowTitle("新邮件")
        self.resize(760,680)
        self.move(300,200)
        self.menu=MenuBar(self)




if __name__ == '__main__':
    import cgitb

    cgitb.enable(format='text')
    a = QApplication(sys.argv)
    m = NewEmail()
    m.show()
    sys.exit(a.exec_())

