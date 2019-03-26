import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from MyButton import *
from MenuWindow import *
from MenuBar import *


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(1000, 600)



        self.setWindowTitle("myMail")
        self.setWindowIcon(QIcon('source/image/myMailIcon.png'))
        self.setFont(QFont("ubuntu", 11))  ##设置字体
        bar = MenuBar(self)

        self.left_menu_panel = MenuWindow(parent=self)



        self.left_menu_panel.move(0, 30)
        self.left_menu_panel.raise_()



if __name__ == "__main__":
    import cgitb

    cgitb.enable(format="text")
    a = QApplication(sys.argv)
    m = MainWindow()
    m.show()
    sys.exit(a.exec_())
