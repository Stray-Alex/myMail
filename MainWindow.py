import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(760, 650)
        self.setWindowTitle("myMail")




if __name__ == "__main__":
    import cgitb

    cgitb.enable(format="text")
    a = QApplication(sys.argv)
    m = MainWindow()
    m.show()
    sys.exit(a.exec_())
