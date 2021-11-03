"""
2021—10-14
今日处理内容：
1). 正在处理中->创建一个线程，按时间打印一个图形
2). 正在处理中->创建一个新窗口，实验画图功能
3). 正在处理中->在画图板种创建多个button，实现快捷绘制
"""
import sys
import re
import _thread
import threading
import time
from time import *
from all_content import *  # all content
from PyQt5.Qt import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Color_Get(QWidget):
    def __init__(self):
        super(Color_Get, self).__init__()
        self.color_1 = QColorDialog.getColor(Qt.white, self, "Select Color")


class Table_Window(QTableWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.t_data = []
        self.headItem = self.horizontalHeaderItem(5)
        self.headerWidth = (60, 60, 40, 40, 100)
        self.ui_layout()  # 启用布局
        self.resizeColumnsToContents()
        # self.get_inf()

    def ui_layout(self):
        """
        self.horizontalHeader().resizeSection(0, 100)
        self.horizontalHeader().resizeSection(1, 100)
        self.horizontalHeader().resizeSection(1, 200)
        """
        self.setWindowTitle('Table')
        self.resize(650, 330)
        # self.setStyle()
        HorizontalHeaderLabels = ["Username", "Password", "Age", "ReadOnly", "More"]
        self.setColumnCount(5)
        self.setRowCount(main.cnt_usr + 1)
        self.setHorizontalHeaderLabels(HorizontalHeaderLabels)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # self.headItem.setIcon(QIcon(":ICON/ICON/retest.png"))  # 设置headItem的图标
        # .setSortingEnabled (self, bool enable)

        for i in range(5):
            self.setColumnWidth(i, self.headerWidth[i])
            item = QTableWidgetItem("示例数据%d" % i)
            # for shuju in (main.usr_name, main.text_pw, main.num_get): pass
            # item = QTableWidgetItem(shuju)
            item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # 设置文本的对齐
            # 设置QTableWidgetItem 的前景色（字体颜色）
            item.setForeground(QColor("red"))
            if i < 4:
                item.setIcon(QIcon('icon/py_icon.png'))  # 设置Item的图标
            elif i == 4:
                item.setIcon(QIcon('icon/del_icon.png'))
            self.setItem(0, i, item)
        self.setEditTriggers(QAbstractItemView.AllEditTriggers)
        for i in range(main.cnt_usr):
            self.setRowHeight(i, 40)

        # This button clear the usr_data.txt!!!
        self.btc = QPushButton(content.btn1_en)
        self.btc.clicked.connect(self.clear_data)
        self.setCellWidget(0, 4, self.btc)
        # self.setCellWidget()

    def clear_data(self):
        reply = QMessageBox.warning(self,
                                    "WARNING!",
                                    "按下'Yes'将导致用户数据全部丢失！",
                                    QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            print('Yes, usr_data.txt is deleted...')
            with open("usr_data.txt", "w+") as f4:
                f4.write("number:0\n")
                main.cnt_usr = 0
        elif reply == QMessageBox.No:
            print('You did a good choice...\n usr_data.txt feels good!')

    def get_inf(self):
        f5 = open('usr_data.txt', 'r')
        # for i in range(main.cnt_usr + 1):
        for u_data in f5.readlines():
            u_data = u_data.strip('\n')
            self.t_data.append(u_data)

        print(self.t_data, type(self.t_data))
        f5.close()

    def set_data(self):
        pass

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
        # self.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
    '''


class Tree_Data(QWidget):
    def __init__(self):
        super(Tree_Data, self).__init__()
        self.setWindowTitle("TreeWidget 例子")
        self.resize(400, 270)
        self.h_data = []
        with open('usr_data.txt', 'r') as f6:
            for u_data in f6.readlines():
                u_data = u_data.strip('\n')
                self.h_data.append(u_data)

        self.tree = QTreeWidget(self)
        # self.data_handle()
        self.tree.setColumnCount(2)
        self.tree.setColumnWidth(0, 180)
        # 设置头的标题
        self.tree.setHeaderLabels(['Key', 'Value'])
        self.root_u = QTreeWidgetItem(self.tree)
        self.root_u.setText(0, 'root_u')
        self.root_u.setText(1, 'user_data')

        self.tree.addTopLevelItem(self.root_u)
        self.tree.clicked.connect(self.onTreeClicked)
        self.addTreeChild()

        treeLayout = QVBoxLayout(self)
        treeLayout.addWidget(self.tree)
        self.setLayout(treeLayout)

    def onTreeClicked(self):
        item = self.tree.currentItem()
        # item.setEditTriggers(self, QAbstractItemView.EditTriggers)
        print("key=%s ,value=%s" % (item.text(0), item.text(1)))

    def addTreeChild(self):
        print("--- addTreeNewChild ---")
        i = 1
        while i <= main.cnt_usr:
            str_1, str_2, str_3 = self.data_handle(i)
            str_num = 'user' + '%d' % i

            n_child = QTreeWidgetItem(self.root_u)
            n_child.setText(0, str_num)
            n_child.setText(1, '%d' % i)
            n_cc1 = QTreeWidgetItem(n_child)
            n_cc1.setText(0, 'username')
            n_cc1.setText(1, str_1)
            n_cc2 = QTreeWidgetItem(n_child)
            n_cc2.setText(0, 'password')
            n_cc2.setText(1, str_2)
            n_cc3 = QTreeWidgetItem(n_child)
            n_cc3.setText(0, 'age')
            n_cc3.setText(1, str_3)
            i += 1

    def data_handle(self, c_u):
        re1 = '(?<=usr:).*?(?=\|)'
        re2 = '(?<=pw:).*?(?=\|)'
        re3 = '(?<=age:).*?(?=\|)'
        pattern_n = re.compile(re1)
        pattern_p = re.compile(re2)
        pattern_a = re.compile(re3)
        str_n = ''.join(re.findall(pattern_n, ''.join(self.h_data[c_u]), flags=0))
        str_p = ''.join(re.findall(pattern_p, ''.join(self.h_data[c_u]), flags=0))
        str_a = ''.join(re.findall(pattern_a, ''.join(self.h_data[c_u]), flags=0))
        print(str_n, str_p, str_a, type(str_n))
        return str_n, str_p, str_a

    def change_data(self):
        pass
    # 直接选中修改value的值，能把修改传递回usr_data.txt
    # self.onTreeClicked()


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
        self.b2 = QCheckBox('')
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
        self.close()

    def bc_2(self):
        self.close()  # click 'Cancle'
        main.close()


class Paint_Draw(QWidget):
    def __init__(self):
        super(Paint_Draw, self).__init__()
        self.qp = QPixmap(600, 600)
        self.setWindowTitle("Paint & Draw")
        # self.qp = QPixmap()
        self.ui_layout()
        # self.paintEvent()

    def ui_layout(self):
        self.resize(600, 600)
        self.qp.fill(Qt.red)
        # self.qp.show()

    def refresh_size(self):
        # 画布尺寸刷新，以适应窗口拖动！
        sa = self.size()
        w = sa.width()
        h = sa.height()
        self.qp = QPixmap(w, h)
        self.qp.fill(Qt.white)

    '''
        def paintEvent(self, event):
        c1 = 0
        #while c1 <= 1.5:
        time.sleep(0.001)
        c1 += 0.001
        print(c1)

    '''


class Main_Window(QMainWindow):
    def __init__(self):
        super(Main_Window, self).__init__()
        self.setWindowTitle('Example of PyQt5')
        self.resize(556, 360)
        self.setFixedSize(self.width(), self.height())
        with open('usr_data.txt', 'a+') as ff:
            ff.seek(0)  # 由于打开方式为'a+'默认指针为文件尾部，所以需要指针置零回到开头部分
            if ff.read(1) == '':
                ff.write("number:0\n")
        with open('usr_data.txt', 'r') as f1:
            gl_n = list(f1.readline())
        self.cnt_usr = int(gl_n[7])
        # print(type(gl_n), gl_n, type(self.cnt_usr), self.cnt_usr)
        self.load_text()
        # print('abc')

        self.cb = QComboBox()
        self.cb.addItem("...")
        self.cb.addItems(["中文", "Français", "Italiano", "日本語"])
        self.cb.setFont(self._fonts)
        self.cb.currentIndexChanged.connect(self.selectionchange)
        self.cb.setStyle(QStyleFactory.create("Fusion"))

        self.create_menu()
        self.creatButton()
        self.create_toolbar()
        self.initUI()
        # self.handle = Data_handle()

    def load_text(self):
        self._font1 = QFont(QFont().defaultFamily(), 25)
        self._font2 = QFont(QFont().defaultFamily(), 18)
        self._font3 = QFont(QFont().defaultFamily(), 10)
        font_s1 = QFont("方正FW筑紫A圆 简 D", 18)
        self._fonts = QFont(font_s1)
        self.text_usr = QLabel(content.con1_en)
        self.text_cbt = QLabel(content.con3_en)
        self.text_tips = QLabel(content.con4_en)
        self.text_num = QLabel(content.btn4_en)
        self.usr_name = QLineEdit()
        self.usr_name.setPlaceholderText("The default")
        self.text_pw = QLineEdit()
        self.text_pw.setReadOnly(True)
        self.num_get = QLineEdit()
        self.num_get.setReadOnly(True)
        self.menu1_1 = content.str_menu1[0]
        self.menu2_1 = content.str_menu2[0]
        self.menu3_1 = content.str_menu3[0]
        for ttt in (self.text_usr, self.text_cbt, self.text_tips, self.usr_name, self.text_pw, self.num_get):
            ttt.setFont(self._fonts)

    def initUI(self):
        h1 = QHBoxLayout()  # Text information & Text box
        h2 = QHBoxLayout()  # Button "password" & password (readonly)
        h3 = QHBoxLayout()  # Button "Age" & number (readonly)
        h4 = QHBoxLayout()  # Tips & ComboBox
        h5 = QHBoxLayout()  # Button "Clear", "Close", "Register", "Tree(Test)"
        for text_all in (self.text_usr, self.usr_name):
            h1.addWidget(text_all, 0, Qt.AlignCenter)
        for text_in in (self.btn3, self.text_pw):
            h2.addWidget(text_in, 0, Qt.AlignCenter | Qt.AlignVCenter)
        for get_num in (self.btn4, self.num_get):
            h3.addWidget(get_num, 0, Qt.AlignCenter | Qt.AlignTop)
        for combo_all in (self.text_cbt, self.cb):
            h4.addWidget(combo_all)
        for btn in (self.btn1, self.btn2, self.btn5, self.btn6):
            h5.addWidget(btn)

        wl = QVBoxLayout(self)
        wl.addLayout(h1)
        wl.addLayout(h2)
        wl.addLayout(h3)
        wl.addLayout(h4)
        wl.addLayout(h5)

        main_frame = QWidget()
        main_frame.setLayout(wl)
        self.setCentralWidget(main_frame)

    def creatButton(self):
        # self.bbb = QPushButton('')
        self.btn1 = QPushButton(content.btn1_en)
        self.btn2 = QPushButton(content.btn2_en)
        self.btn3 = QPushButton(content.btn3_en)
        self.btn4 = QPushButton(content.btn4_en)
        self.btn5 = QPushButton(content.btn5_en)
        self.btn6 = QPushButton(content.btn6_en)
        self.btn1.clicked.connect(self.clear_btn)
        self.btn2.clicked.connect(self.close_main)
        self.btn3.clicked.connect(self.pw_btn)
        self.btn4.clicked.connect(self.number_btn)
        self.btn5.clicked.connect(self.reg_btn)
        self.btn6.clicked.connect(self.tree_btn)
        for bbb in (self.btn1, self.btn2, self.btn3, self.btn4, self.btn5, self.btn6):
            bbb.setFont(self._fonts)
            bbb.setStyle(QStyleFactory.create("Fusion"))

    def echo(self, value):
        """显示对话框返回值"""
        QMessageBox.information(self, "返回值", "得到：{}\n\ntype: {}".format(value, type(value)),
                                QMessageBox.Yes | QMessageBox.No)

    def clear_btn(self):
        self.usr_name.clear()
        self.text_pw.clear()
        self.num_get.clear()
        print("Clear!")

    def close_main(self):
        print('Close!')
        self.close()

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
        for j_g in (self.usr_name.text(), self.text_pw.text(), self.num_get.text()):
            if len(j_g) == 0:
                sta = 0
                break
            elif len(j_g) != 0:
                sta = 1
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
        if self.judge_blanc() == 0:
            self.cnt_usr -= 1
        elif self.judge_blanc() == 1:
            self.change_num()
            self.writing_data()
            self.open_table()

    def change_num(self):
        with open('usr_data.txt', 'r+') as f2:
            gt = f2.read()
        gt_l = list(gt)
        gt_l[7] = '%d' % self.cnt_usr
        gt2 = ''.join(gt_l)
        with open('usr_data.txt', 'w+') as f3:
            f3.write(gt2)

    def selectionchange(self, text_content=None):
        self.langue = self.cb.currentText()
        # main_new = Draw_Window()
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
        exitButton = QAction(QIcon('./icon/exit_1.jpg'), 'Exit', self)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.triggered.connect(self.close)
        tableButton = QAction(QIcon('./icon/table_1.png'), 'Table', self)
        tableButton.setShortcut('Ctrl+T')
        tableButton.triggered.connect(self.open_table)
        drawButton = QAction(QIcon('./icon/paint_icon.jpg'), "Paint", self)
        drawButton.setShortcut('Ctrl+D')
        drawButton.triggered.connect(self.paint_sth)
        toolbar_turn = QAction('Toolbar', self, checkable=True)
        toolbar_turn.setChecked(True)
        toolbar_turn.triggered.connect(self.toolbar_t)

        agButton = QAction('O_A', self)
        agButton.triggered.connect(self.open_ag)

        menu1 = menubar.addMenu(self.menu1_1)
        # menu1.addAction(QAction("New", self, self.table.show()))  # 带图标，文字
        menu1.addAction(agButton)
        menu1.addAction("Close")
        menu1_1 = menu1.addMenu("Try")
        menu1_1.addAction("copy")
        menu1_1.addAction("paste")
        menu1.addSeparator()
        menu1.addAction(QAction(QIcon('./icon/f8.png'), "Save", self))
        menu1.addAction(exitButton)
        menu1.addAction(tableButton)

        menu2 = menubar.addMenu(self.menu2_1)
        menu2.addAction(QAction("Delete", self))
        menu2.addSeparator()
        menu2.addAction(drawButton)

        menu3 = menubar.addMenu(self.menu3_1)
        menu3.addAction(toolbar_turn)

    def open_table(self):
        self.table = Table_Window()
        self.table.get_inf()
        self.table.show()

    def toolbar_t(self, state):
        print("'toolbar' is clicked, the state is:", state, type(state))
        if not state:
            self.toolbar.setHidden(True)
        elif state:
            self.toolbar.setHidden(False)

    def open_ag(self):
        ag = Agreement_Box()
        ag.show()

    '''
    | Save | Close | ... |
    '''

    def create_toolbar(self):
        self.toolbar = self.addToolBar('1')
        # self.toolbar.setStyle(QStyleFactory.create("Fusion"))
        paint_bar = QAction(QIcon('./icon/paint_icon.jpg'), "Paint", self)
        table_bar = QAction(QIcon('./icon/table_1.png'), "Table", self)
        self.toolbar.addAction(paint_bar)
        self.toolbar.addAction(table_bar)
        self.toolbar.addSeparator()
        self.toolbar.actionTriggered[QAction].connect(self.toolbtnpressed)

        self.toolbar2 = self.addToolBar('2')
        blanc_1 = QAction('', self)
        blanc_2 = QAction('', self)
        self.toolbar2.addAction(blanc_1)
        self.toolbar2.addAction(blanc_2)
        self.toolbar2.setMovable(False)
        # self.toolbar2.setEnabled(False)
        self.toolbar2.setStyleSheet('QToolBar{background: red; spacing: 50px}')

        self.toolbar3 = self.addToolBar('3')
        close_bar = QAction(QIcon('./icon/py_icon.png'), "Close", self)
        self.toolbar3.addAction(close_bar)
        self.toolbar3.setMovable(False)

        # self.create_toolbar = QAction()


        


    def toolbtnpressed(self, a):
        print("Push the toolbar button:", a.text())
        if a.text() == "Table":
            self.open_table()
        elif a.text() == "Paint":
            self.paint_sth()

    def writing_data(self):
        f = open('usr_data.txt', 'a')
        tt = ['usr:', self.usr_name.text(), '|', 'pw:', self.text_pw.text(), '|', 'age:', self.num_get.text(), '|\n']
        str1 = ''.join(tt)
        f.write(str1)
        f.close()

    def tree_btn(self):
        self.rtree = Tree_Data()
        self.rtree.show()

    def paint_sth(self):
        # todo: here, we create a button which when you click it will create a pixmap and you can draw sth. on it.
        self.p_d = Paint_Draw()
        self.p_d.show()

    # def print_time(threadName):pass
    '''
    @staticmethod
    def thread_it(func, *args):
        t = threading.Thread(target=func, args=args)
        t.setDaemon(True)  # 守护--就算主界面关闭，线程也会留守后台运行（不对!）
        t.start()  # 启动
    '''


if __name__ == "__main__":
    app = QApplication(sys.argv)
    content = Text_Content()
    main = Main_Window()
    main.show()
    sys.exit(app.exec_())
