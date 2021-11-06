#
#  创建一个新的窗口，分成如下形式
#   ---------------
#  |      |   2    |
#  |   1  |--------|
#  |      |   3    |
#   ---------------
#  要求：3区域可以隐藏
#  2区域可以延展至原先的3区域
#
import sys
import re
import _thread
import threading
import time
from time import *

from PyQt5.Qt import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Main_Window(QMainWindow):
    def __init__(self):
        super(Main_Window, self).__init__()
        self.setWindowTitle('Hide_Me')
        self.resize(1760, 800)
        self.create_toolbar()
        self.initUI()

    def initUI(self):
        self.workpannel = QFrame(self)
        hbox = QHBoxLayout(self.workpannel)
        self.setCentralWidget(self.workpannel)

        splitter1 = QSplitter(Qt.Horizontal)
        textedit_1 = QTextEdit()
        splitter1.addWidget(textedit_1)
        splitter1.setSizes([100, 200])

        splitter2 = QSplitter(Qt.Vertical)
        textedit_2 = QTextEdit()
        textedit_3 = QTextEdit()
        # splitter2.addWidget()
        # splitter2.addWidget(textedit_3)
        splitter4 = QSplitter()
        splitter5 = QSplitter()
        splitter4.addWidget(textedit_2)
        splitter5.addWidget(textedit_3)

        splitter2.addWidget(splitter4)
        splitter2.addWidget(splitter5)
        # splitter2.addWidget(bottom)

        splitter3 = QSplitter(self)
        splitter3.addWidget(splitter1)
        splitter3.addWidget(splitter2)
        splitter3.setOrientation(Qt.Horizontal)

        hbox.addWidget(splitter3)
        self.workpannel.setLayout(hbox)

        # QApplication.setStyle(QStyleFactory.create('Cleanlooks'))

    def create_toolbar(self):
        self.toolbar = self.addToolBar('1')
        paint_bar = QAction(QIcon('./icon/paint_icon.jpg'), "Paint", self)
        table_bar = QAction(QIcon('./icon/table_1.png'), "Table", self)
        self.toolbar.addAction(paint_bar)
        self.toolbar.addAction(table_bar)
        self.toolbar.addSeparator()
        # self.toolbar.actionTriggered[QAction].connect(self.toolbtnpressed)

        self.toolbar2 = self.addToolBar('2')
        blanc_1 = QAction('', self)
        blanc_2 = QAction('', self)
        self.toolbar2.addAction(blanc_1)
        self.toolbar2.addAction(blanc_2)
        self.toolbar2.setMovable(False)
        self.toolbar2.setEnabled(False)
        self.toolbar2.setStyleSheet('QToolBar{background: gray; spacing: 50px}')

        self.toolbar3 = self.addToolBar('3')
        close_bar = QAction(QIcon('./icon/py_icon.png'), "Close", self)
        self.toolbar3.addAction(close_bar)
        self.toolbar3.setMovable(False)

        # self.create_toolbar = QAction()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main_Window()
    main.show()
    sys.exit(app.exec_())
