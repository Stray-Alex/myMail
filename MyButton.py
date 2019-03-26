# -*- coding: utf-8 -*-
# @Time    : 19-3-26 下午2:43
# @Author  : YanPengliang
# @Project : myMail
# @File    : MyButton.py
# @Version : v1.0

from PyQt5 import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys


class MyButton(QLabel):
    def __init__(self, *args, parent=None):
        super().__init__(parent)

        self.hoverPixmap = QPixmap(args[0])
        self.normalPixmap = QPixmap(args[1])
        self.pressPixmap = QPixmap(args[2])

        self.enterState = False
        self.setPixmap(self.normalPixmap)
        self.setFixedSize(self.normalPixmap.size())

        def mouseReleaseEvent(self, ev: QtGui.QMouseEvent):
            if self.enterState == False:
                self.setPixmap(self.normalPixmap)
            else:
                self.setPixmap(self.hoverPixmap)

            # print("鼠标释放")
            self.clicked.emit()  # 发射信号

        def mousePressEvent(self, ev: QtGui.QMouseEvent):
            self.setPixmap(self.pressPixmap)
            # print("鼠标按下")
            pass

        def enterEvent(self, a0: QtCore.QEvent):
            self.setPixmap(self.hoverPixmap)
            self.enterState = True
            # print("鼠标进入")
            pass

        def leaveEvent(self, a0: QtCore.QEvent):
            self.setPixmap(self.normalPixmap)
            self.enterState = False
            # print("鼠标离开")
            pass

if __name__ == '__main__':
    import cgitb

    # 防止程序异常退出
    cgitb.enable(format='text')
    a = QApplication(sys.argv)
    mybtn = MyButton('source/image/newMail.png',
                     'source/image/newMail.png',
                     'source/image/newMail.png')
    mybtn.show()
    sys.exit(a.exec_())
