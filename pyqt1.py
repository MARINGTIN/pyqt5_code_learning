"""
2021—10-10
今日待定处理内容：
1).保证表格正常打开放置
2).保证数据传输
3).
"""

import sys
from all_content import *  # all content
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Color_Get(QWidget):

    def __init__(self):
        super(Color_Get, self).__init__()
        self.color_get1 = QColorDialog.getColor(Qt.white, self, "Select Color")


data1 = {'Username': ['1-1', '1-2', '1-3', '1-4'],
         'Password': ['2-1', '2-2', '2-3', '2-4'],
         'Age': ['3-1', '3-2', '3-3', '3-4']}


# --------------------------------- #
#   0  | username | password | age  #
# --------------------------------- #
#   1  |          |          |      #
# --------------------------------- #
class Table_Window(QTableWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.headItem = self.horizontalHeaderItem(5)
        self.headerWidth = (60, 60, 40, 40, 100)

        self.ui_layout()

        self.resizeColumnsToContents()
        # self.resizeRowsToContents()

    def ui_layout(self):
        """
        self.horizontalHeader().resizeSection(0, 100)
        self.horizontalHeader().resizeSection(1, 100)
        self.horizontalHeader().resizeSection(1, 200)
        """
        self.setWindowTitle('Table')
        self.resize(500, 300)
        HorizontalHeaderLabels = ["Username", "Password", "Age", "Serial", "More"]
        self.setColumnCount(5)
        self.setRowCount(main.cnt_usr + 1)
        self.setHorizontalHeaderLabels(HorizontalHeaderLabels)

        print("check table2", main.cnt_usr)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # self.headItem.setIcon(QIcon(":ICON/ICON/retest.png"))  # 设置headItem的图标

        # .setSortingEnabled (self, bool enable)

        for i in range(5):
            self.setColumnWidth(i, self.headerWidth[i])
            #item = QTableWidgetItem("示例数据%d" % i)
            for shuju in (main.usr_name, main.text_pw, main.num_get):
                item = QTableWidgetItem(shuju)
            item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # 设置文本的对齐
            # 设置QTableWidgetItem 的前景色（字体颜色）
            item.setForeground(QColor("red"))
            item.setIcon(QIcon("py_icon.png"))  # 设置Item的图标
            self.setItem(0, i, item)
            #item1 = QTableWidgetItem()
            #self.setItem(1, i, item1)

        self.setEditTriggers(QAbstractItemView.AllEditTriggers)

        for i in range(main.cnt_usr):
            self.setRowHeight(i, 40)

    '''
    def setData(self):
        horHeaders = []
        for n, key in enumerate(sorted(self.data1.keys())):
            horHeaders.append(key)
            print(horHeaders)
            for m, item in enumerate(self.data1[key]):
                newitem = QTableWidgetItem(item)
                # newitem.setIcon(QIcon("f8.png"))  # 设置Item的图标
                self.setItem(m, n, newitem)
        print(horHeaders)
        self.setHorizontalHeaderLabels(horHeaders)
        #
        #self.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)


    def judge_blanc(self):
        """ Return bool_ to judge whether there are blanc among username, password & age."""
        print("judge?")
        for j_g in (main.usr_name.text(), main.text_pw.text(), main.num_get.text()):
            if len(j_g) == 0:
                sta = 0
                break
            elif len(j_g) != 0:
                sta = 1
        # print(sta)
        if sta == 0:
            self.warning_close()
            return 0
        elif sta == 1:
            return 1

    def warning_close(self):
        QMessageBox.warning(self,
                            content.mes1_cn,
                            content.mes2_cn,
                            QMessageBox.Yes | QMessageBox.No)



    def get_inf(self):
        newitem_ = QTableWidgetItem(main.usr_name.text())
        # self.setItem(3, 3, newitem_)

    '''


class Check_Box(QWidget):
    def __init__(self, parent=None):
        super(Check_Box, self).__init__(parent)
        layout = QHBoxLayout()
        self.b1 = QCheckBox("Button1")
        self.b1.setChecked(True)
        self.b1.stateChanged.connect(lambda: self.btnstate(self.b1))
        layout.addWidget(self.b1)

        self.b2 = QCheckBox("Button2")
        self.b2.toggled.connect(lambda: self.btnstate(self.b2))

        layout.addWidget(self.b2)
        self.setLayout(layout)
        self.setWindowTitle("checkbox demo")

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


class Main_Window(QMainWindow):
    def __init__(self):
        super(Main_Window, self).__init__()
        self.cnt_usr = 0
        self._font1 = QFont(QFont().defaultFamily(), 25)
        self._font2 = QFont(QFont().defaultFamily(), 18)
        self._font3 = QFont(QFont().defaultFamily(), 10)
        # self._font4 = QFont(QFont().defaultFamily(), )

        self.text_usr = QLabel(content.con1_en)
        self.text_usr.setFont(self._font2)
        self.text_cbt = QLabel(content.con3_en)
        self.text_cbt.setFont(self._font2)
        self.text_tips = QLabel(content.con4_en)
        self.text_tips.setFont(self._font2)
        self.text_num = QLabel(content.btn4_en)
        self.usr_name = QLineEdit()
        self.usr_name.setPlaceholderText("The default")
        self.usr_name.setFont(self._font2)
        self.text_pw = QLineEdit()
        self.text_pw.setFont(self._font2)
        self.text_pw.setReadOnly(True)
        self.num_get = QLineEdit()
        self.num_get.setFont(self._font2)
        self.num_get.setReadOnly(True)
        self.menu1_1 = content.str_menu1[0]
        self.menu2_1 = content.str_menu2[0]
        self.menu3_1 = content.str_menu3[0]

        self.cb = QComboBox()
        self.cb.addItem("...")
        self.cb.addItems(["中文", "Français", "Italiano", "日本語"])
        self.cb.setFont(self._font2)
        self.cb.currentIndexChanged.connect(self.selectionchange)

        # self.menu1_l = [content.menu1_en, content.menu1_cn]
        # self.menu1 = self.menu1_l[0]

        self.create_menu()
        self.creatButton()
        # self.create_toolbar()
        self.initUI()

    # noinspection PyArgumentList
    def initUI(self):
        self.setWindowTitle('Example of PyQt5')
        self.resize(556, 270)
        wl = QVBoxLayout(self)
        h1 = QHBoxLayout()  # Text information & Text box
        h2 = QHBoxLayout()  # Text information & password (readonly)
        h3 = QHBoxLayout()  # Text information & number (readonly)
        h4 = QHBoxLayout()  # Tips & ComboBox
        h5 = QHBoxLayout()  # Button "Clear", "Close", "password", "number"
        wl.addLayout(h1)
        wl.addLayout(h2)
        wl.addLayout(h3)
        wl.addLayout(h4)
        wl.addLayout(h5)
        for text_all in (self.text_usr, self.usr_name):
            h1.addWidget(text_all, 0, Qt.AlignLeft | Qt.AlignCenter)
        for text_in in (self.btn3, self.text_pw):
            h2.addWidget(text_in, 0, Qt.AlignCenter | Qt.AlignVCenter)
        for get_num in (self.btn4, self.num_get):
            h3.addWidget(get_num, 0, Qt.AlignCenter | Qt.AlignTop)
        for combo_all in (self.text_cbt, self.cb):
            h4.addWidget(combo_all)
        for btn in (self.btn1, self.btn2, self.btn5):
            h5.addWidget(btn)

        main_frame = QWidget()
        main_frame.setLayout(wl)
        self.setCentralWidget(main_frame)
        self.show()

    def creatButton(self):
        self.btn1 = QPushButton(content.btn1_en)
        self.btn1.setFont(self._font2)
        self.btn2 = QPushButton(content.btn2_en)
        self.btn2.setFont(self._font2)
        self.btn3 = QPushButton(content.btn3_en)
        self.btn3.setFont(self._font2)
        self.btn4 = QPushButton(content.btn4_en)
        self.btn4.setFont(self._font2)
        self.btn5 = QPushButton(content.btn5_en)
        self.btn5.setFont(self._font2)
        self.btn1.clicked.connect(self.clear_btn)
        self.btn2.clicked.connect(self.close)
        self.btn3.clicked.connect(self.pw_btn)
        self.btn4.clicked.connect(self.number_btn)
        self.btn5.clicked.connect(self.reg_btn)

    def echo(self, value):
        """显示对话框返回值"""
        QMessageBox.information(self, "返回值", "得到：{}\n\ntype: {}".format(value, type(value)),
                                QMessageBox.Yes | QMessageBox.No)

    def clear_btn(self):
        self.usr_name.clear()
        self.text_pw.clear()
        self.num_get.clear()
        print("Clear!")

    def pw_btn(self):  # 输入：文本
        value, ok = QInputDialog.getText(self, "Password", self.text_tips.text(), QLineEdit.Normal, "Default_0")
        if ok:
            # self.echo(value)
            self.text_pw.setText(value)
            self.text_pw.setContextMenuPolicy(Qt.NoContextMenu)
            self.text_pw.setEchoMode(QLineEdit.Password)
        else:
            self.echo(value)

    def number_btn(self):
        num1, ok = QInputDialog.getInt(self, "Get number", self.text_num.text(), QLineEdit.Normal, 0)
        if ok:
            numlist = str(num1)
            self.num_get.setText(numlist)

    def judge_blanc(self):
        """ Return bool_ to judge whether there are blanc among username, password & age."""
        print("judge?")
        for j_g in (self.usr_name.text(), self.text_pw.text(), self.num_get.text()):
            if len(j_g) == 0:
                sta = 0
                break
            elif len(j_g) != 0:
                sta = 1
        # print(sta)
        if sta == 0:
            self.warning_close()
            return 0
        elif sta == 1:
            return 1

    def warning_close(self):
        QMessageBox.warning(self,
                            content.mes1_cn,
                            content.mes2_cn,
                            QMessageBox.Yes | QMessageBox.No)

    def reg_btn(self):
        self.cnt_usr += 1
        print(self.cnt_usr)
        # self.table.get_inf()
        if self.judge_blanc() == 0:
            self.cnt_usr -= 1
        elif self.judge_blanc() == 1:
            self.table = Table_Window()
            self.table.show()

    def selectionchange(self, text_content=None):
        self.langue = self.cb.currentText()
        # main_new = Main_Window()
        if self.langue == '中文':
            print("Choose Chinese")
            self.text_usr.setText(content.con1_cn)
            self.text_cbt.setText(content.con3_cn)
            self.text_tips.setText(content.con4_cn)
            self.text_num.setText(content.btn4_cn)
            self.btn1.setText(content.btn1_cn)
            self.btn2.setText(content.btn2_cn)
            self.btn3.setText(content.btn3_cn)
            self.btn4.setText(content.btn4_cn)
            self.btn5.setText(content.btn5_cn)
            self.menu1_1 = content.str_menu1[1]

            # main_new.show()

        elif self.langue == '...':
            # print("... mode")
            self.text_usr.setText(content.con1_en)
            self.text_cbt.setText(content.con3_en)
            self.text_tips.setText(content.con4_en)
            self.text_num.setText(content.btn4_en)
            self.btn1.setText(content.btn1_en)
            self.btn2.setText(content.btn2_en)
            self.btn3.setText(content.btn3_en)
            self.btn4.setText(content.btn4_en)
            self.btn5.setText(content.btn5_en)
            # self.menu1 = self.menu1_l[0]
            # main_new.show()

    def create_menu(self):
        menubar = self.menuBar()
        menu1 = menubar.addMenu(self.menu1_1)
        menu1.addAction(QAction("New", self, triggered=qApp.quit))  # 带图标，文字
        menu1.addAction(QAction("Open", self, triggered=qApp.quit))
        menu1.addAction("Close")
        menu1_1 = menu1.addMenu("Try")
        menu1_1.addAction("copy")
        menu1_1.addAction("paste")
        menu1.addSeparator()
        menu1.addAction(QAction(QIcon("f8.png"), "Save", self, triggered=qApp.quit))
        menu1.addAction(QAction(QIcon("exit_1.jpg"), "Exit", self, triggered=qApp.quit))

        menu2 = menubar.addMenu(self.menu2_1)
        menu2.addAction(QAction("Delete", self))

        menu3 = menubar.addMenu(self.menu3_1)
        menu3.addAction(QAction("Toolbar", self))

    '''
    | Save | Close | ... |
    '''

    def create_toolbar(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    content = Text_Content()
    main = Main_Window()
    main.show()
    sys.exit(app.exec_())