# -*- coding: utf-8 -*-
# @Time    : 19-3-26 下午4:10
# @Author  : YanPengliang
# @Project : myMail
# @File    : MenuWindow.py
# @Version : v1.0

from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from MyButton import MyButton
import sys


class MenuWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(300, 1080)

        self.new_email_btn = MyButton('source/image/newMail3.png',
                                      'source/image/newMail.png',
                                      'source/image/newMail2.png', parent=self)
        self.new_email_btn.move(10, 30)

        self.receive_email_btn = MyButton('source/image/receiveMail3.png',
                                          'source/image/receiveMail.png',
                                          'source/image/receiveMail2.png', parent=self)
        self.receive_email_btn.move(10, 90)

        self.address_list_btn = MyButton('source/image/addressList3.png',
                                         'source/image/addressList.png',
                                         'source/image/addressList2.png', parent=self)
        self.address_list_btn.move(10, 150)


if __name__ == '__main__':
    import cgitb

    cgitb.enable(format='text')
    a = QApplication(sys.argv)
    m = MenuWindow()
    m.show()
    sys.exit(a.exec_())
