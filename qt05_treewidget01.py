"""
    【简介】
    PyQT5中 QTreeWidget 例子


"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QBrush, QColor
from PyQt5.QtCore import Qt


class TreeWidgetDemo(QMainWindow):
    def __init__(self, parent=None):
        super(TreeWidgetDemo, self).__init__(parent)
        self.setWindowTitle('TreeWidget 例子')
        self.tree = QTreeWidget()
        self.resize(400, 200)
        # 设置列数
        self.tree.setColumnCount(2)
        # 设置头的标题
        self.tree.setHeaderLabels(['Key', 'Value'])
        # 设置根节点
        root = QTreeWidgetItem(self.tree)
        root.setText(0, 'root')
        root.setIcon(0, QIcon("./icon/root.png"))
        # 设置列宽
        self.tree.setColumnWidth(0, 180)

        # 设置节点的背景颜色
        brush_red = QBrush(Qt.red)
        root.setBackground(0, brush_red)
        brush_green = QBrush(Qt.green)
        root.setBackground(1, brush_green)

        # 设置子节点1
        child1 = QTreeWidgetItem(root)
        child1.setText(0, 'child1')
        child1.setText(1, 'ios')
        child1.setIcon(0, QIcon("./icon/IOS.png"))
        # child1.setCheckState(0, Qt.Checked)

        child1_1 = QTreeWidgetItem(child1)
        child1_1.setText(0, 'child1_1')
        child1_1.setText(1, '')
        child1_1.setIcon(0, QIcon("./icon/music.png"))

        # 设置子节点2
        child2 = QTreeWidgetItem(root)
        child2.setText(0, 'child2')
        child2.setText(1, 'android')
        child2.setIcon(0, QIcon("./icon/android.png"))

        # 设置子节点2_1
        child2_1 = QTreeWidgetItem(child2)
        child2_1.setText(0, 'child2_1')
        child2_1.setText(1, '')
        child2_1.setIcon(0, QIcon("./icon/music.png"))

        self.tree.addTopLevelItem(root)
        # 结点全部展开
        self.tree.expandAll()

        self.setCentralWidget(self.tree)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    tree = TreeWidgetDemo()
    tree.show()
    sys.exit(app.exec_())
