"""
    【简介】
    PyQT5中 QTreeView 例子


"""

import sys
from PyQt5.QtWidgets import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # Window系统提供的模式
    model = QDirModel()
    # 创建一个QTreeView部件
    tree = QTreeView()
    # 为部件添加模式
    tree.setModel(model)
    tree.setWindowTitle('QTreeView 例子')
    tree.resize(640, 400)
    tree.show()
    sys.exit(app.exec_())
