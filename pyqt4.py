import sys
import re
from PyQt5.Qt import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from all_content import *  # all content


class Agreement_Box(QWidget):
    def __init__(self, parent=None):
        super(Agreement_Box, self).__init__(parent)
        self.setWindowTitle("Agreement")
        self.resize(500, 200)
        layout = QVBoxLayout()
        self.ag_txt = QLabel(content.agq_en)
        self.ag_cnt = QTextEdit()
        self.ag_cnt.setPlainText(content.agt_en)
        self.ag_cnt.setReadOnly(True)

        self.b1 = QCheckBox("male")
        self.b1.setChecked(True)
        self.b1.stateChanged.connect(lambda: self.btnstate(self.b1))
        self.b2 = QCheckBox("")
        self.b2.toggled.connect(lambda: self.btnstate(self.b2))
        self.r1 = QRadioButton(content.qr1_en)
        self.r2 = QRadioButton(content.qr2_en)
        self.setLayout(layout)
        # self.setWindowTitle("checkbox demo")
        layout.addWidget(self.ag_txt)
        layout.addWidget(self.ag_cnt)
        layout.addWidget(self.b1)
        layout.addWidget(self.r1)
        layout.addWidget(self.r2)
        # layout.addWidget(self.b2)

    def btnstate(self, b):
        if b.text() == "Button1":
            if b.isChecked():
                print(b.text() + " is selected")
            else:
                print(b.text() + " is deselected")
        if b.text() == "Button2":
            if b.isChecked():
                print(b.text() + " is selected")
            else:
                print(b.text() + " is deselected")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    content = Text_Content()
    main = Agreement_Box()
    main.show()
    sys.exit(app.exec_())
