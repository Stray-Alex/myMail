import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MenuBar(QMenuBar):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(1920, 28)
        self.setFont(QFont("ubuntu", 11))  # 设置字体


        file = self.addMenu('文件')
        view = self.addMenu('视图')
        window = self.addMenu("窗口")
        tools = self.addMenu("工具")
        help = self.addMenu("帮助")

        file.setFont(QFont("ubuntu", 11))
        view.setFont(QFont("ubuntu", 11))
        window.setFont(QFont("ubuntu", 11))
        tools.setFont(QFont("ubuntu", 11))
        help.setFont(QFont("ubuntu", 11))

        # 向QMenu小控件中添加按钮，子菜单
        file.addAction('新建')

        # 定义响应小控件按钮，并设置快捷键关联到操作按钮，添加到父菜单下
        save = QAction('保存', self)
        save.setShortcut('Ctrl+S')
        file.addAction(save)

        # 创建新的子菜单项，并添加孙菜单
        edit = file.addMenu('编辑')
        edit.addAction('复制')
        edit.addAction('粘贴')

        help.addAction("关于...")

        # 添加父菜单下
        quit = QAction('Quit', self)
        file.addAction(quit)

        # 单击任何Qmenu对象，都会发射信号，绑定槽函数
        file.triggered[QAction].connect(self.processtrigger)

    def processtrigger(self, q):
        # 输出那个Qmenu对象被点击
        print(q.text() + 'is triggeres')
