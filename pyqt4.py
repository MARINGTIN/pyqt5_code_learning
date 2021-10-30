import sys
import re
from PyQt5.Qt import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from all_content import *  # all content
'''
该功能是一个测试radiobutton和checkbox
以及禁用和启用pushbutton的测试窗口
'''


class Agreement_Box(QWidget):
    def __init__(self, parent=None):
        super(Agreement_Box, self).__init__(parent)
        self.setWindowTitle("Agreement")
        self.resize(500, 200)
        l1 = QVBoxLayout()
        l1_1 = QHBoxLayout()
        self.ag_txt = QLabel(content.agq_en)
        self.ag_cnt = QTextEdit()
        self.ag_cnt.setPlainText(content.agt_en)
        self.ag_cnt.setReadOnly(True)

        self.b1 = QCheckBox("I've already read above all, and I'm already aware of the risk.")
        self.b1.setChecked(False)
        self.b1.stateChanged.connect(lambda: self.btnstate(self.b1))
        self.b2 = QCheckBox("")
        self.b2.toggled.connect(lambda: self.btnstate(self.b2))
        self.r1 = QRadioButton(content.qr1_en)
        self.r1.toggled.connect(lambda: self.btnstate(self.r1))
        self.r1.setEnabled(False)
        self.r2 = QRadioButton(content.qr2_en)
        self.r2.toggled.connect(lambda: self.btnstate(self.r2))

        self.bb1 = QPushButton("Next")
        self.bb1.setEnabled(False)
        self.bb1.clicked.connect(self.bc_1)
        self.bb2 = QPushButton("Cancel")
        self.bb2.setEnabled(True)
        self.bb2.clicked.connect(self.bc_2)

        self.setLayout(l1)
        # self.setWindowTitle("checkbox demo")
        l1.addWidget(self.ag_txt)
        l1.addWidget(self.ag_cnt)
        l1.addWidget(self.b1)
        l1.addWidget(self.r1)
        l1.addWidget(self.r2)
        l1_1.addWidget(self.bb1)
        l1_1.addWidget(self.bb2)
        l1.addLayout(l1_1)

    def btnstate(self, b):
        if b.text() == content.qr1_en:
            if b.isChecked():
                print("qr1 is selected")
                self.bb1.setEnabled(True)
            else:
                print("qr1 is deselected")
                self.bb1.setEnabled(False)
        if b.text() == content.qr2_en:
            if b.isChecked():
                print("qr2 is selected")
            else:
                print("qr2 is deselected")
        if b.text() == "I've already read above all, and I'm already aware of the risk.":
            if b.isChecked():
                self.r1.setEnabled(True)
                self.b1.setDisabled(True)

    def bc_1(self):
        print("clicked 'Next'")

    def bc_2(self):
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    content = Text_Content()
    main = Agreement_Box()
    main.show()
    sys.exit(app.exec_())
