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
import numpy as np

# import matplotlib.pyplot as plot

list_data2 = [0.00, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09,
              0.10, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19,
              0.2, 0.3, 0.4, 0.6, 0.8, 1, 1, 1.3, 1.6, 2, 2.4, 2.8, 3, 3.5, 4,
              1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
              1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
              1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
              1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
              1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
              2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
              4.40, 4.41, 4.42, 4.43, 4.44, 4.45, 4.46, 4.47, 4.48, 4.49,
              4.50, 4.51, 4.52, 4.53, 4.58, 4.59,
              4.60, 4.61, 4.62, 4.63, 4.64, 4.65, 4.66, 4.67, 4.68, 4.69,
              4.70, 4.71, 4.72, 4.73, 4.74, 4.75, 4.76, 4.77, 4.78]

list_data = [0.0000, 0.0000, 0.0100, 0.0198, 0.0296, 0.0392, 0.0488, 0.0583, 0.0677,
             0.0770, 0.0862, 0.0953, 0.1044, 0.1133, 0.1222, 0.1310, 0.1398, 0.1484, 0.1570,
             0.1655, 0.1740, 0.1823, 0.1906, 0.1989, 0.2070, 0.2151, 0.2231, 0.2311, 0.2390,
             0.2469, 0.2546, 0.2624, 0.2700, 0.2776, 0.2852, 0.2927, 0.3001, 0.3075, 0.3148,
             0.3221, 0.3293, 0.3365, 0.3436, 0.3507, 0.3577, 0.3646, 0.3716, 0.3784, 0.3853, 0.3920, 0.3988, 0.4055,
             0.4121, 0.4187, 0.4253, 0.4318, 0.4383, 0.4447, 0.4511, 0.4574, 0.4637, 0.4700, 0.4762, 0.4824, 0.4886,
             0.4947, 0.5008, 0.5068, 0.5128, 0.5188, 0.5247, 0.5306, 0.5365, 0.5423, 0.5481, 0.5539, 0.5596, 0.5653,
             0.5710, 0.5766, 0.5822, 0.5878, 0.5933, 0.5988, 0.6043, 0.6098, 0.6152, 0.6206, 0.6259, 0.6313, 0.6366,
             0.6419, 0.6471, 0.6523, 0.6575, 0.6627, 0.6678, 0.6729, 0.6780, 0.6831, 0.6881, 0.6931, 0.6981, 0.7031,
             1.0784, 1.0818, 1.0852, 1.0886, 1.0919, 1.0953, 1.0986, 1.1019, 1.1053, 1.1086, 1.1119, 1.1151, 1.1184,
             1.1217, 1.1249, 1.1282, 1.1314, 1.1346, 1.1378, 1.1410, 1.1442, 1.1474, 1.1506, 1.1537, 1.1569, 1.1600,
             1.1632, 1.1663, 1.1694, 1.1725, 1.1756, 1.1787, 1.1817, 1.1848, 1.1878, 1.1909, 1.1939, 1.1969, 1.2000,
             1.2030, 1.2060, 1.2090, 1.2119, 1.2149, 1.2179, 1.2208, 1.2238, 1.2267, 1.2296, 1.2326, 1.2355, 1.2384,
             1.2413, 1.2442, 1.2470, 1.2499, 1.2528, 1.2556, 1.2585, 1.2613, 1.2641, 1.2669, 1.2698, 1.2726, 1.2754,
             1.2782, 1.2809, 1.2837, 1.2865, 1.2892, 1.2920, 1.2947, 1.2975, 1.3002, 1.3029, 1.3056, 1.3083, 1.3110,
             1.3137, 1.3164, 1.3191, 1.3218, 1.3244, 1.3271, 1.3297, 1.3324, 1.3350, 1.3376, 1.3403, 1.3429, 1.3455,
             1.3481, 1.3507, 1.3533, 1.3558, 1.3584, 1.3610, 1.3635, 1.3661, 1.3686, 1.3712, 1.3737, 1.3762, 1.3788,
             1.3813, 1.3838, 1.3863, 1.3888, 1.3913, 1.3938, 1.3962, 1.3987, 1.4012, 1.4036, 1.4061, 1.4085, 1.4110,
             1.4134, 1.4159, 1.4183, 1.4207, 1.4231, 1.4255, 1.4279, 1.4303, 1.4327, 1.4351, 1.4375, 1.4398, 1.4422,
             1.4446, 1.4469, 1.4493, 1.4516, 1.4540, 1.4563, 1.4586, 1.4609, 1.4633, 1.4656, 1.4679, 1.4702, 1.4725,
             1.4748, 1.4770, 1.4793, 1.4816, 1.4839, 1.4861, 1.4884, 1.4907, 1.4929, 1.4951, 1.4974, 1.4996, 1.5019,
             1.5041, 1.5063, 1.5085, 1.5107, 1.5129, 1.5151, 1.5173, 1.5195, 1.5217, 1.5239, 1.5261, 1.5282, 1.5304,
             1.5326, 1.5347, 1.5369, 1.5390, 1.5412, 1.5433, 1.5454, 1.5476, 1.5497, 1.5518, 1.5539, 1.5560, 1.5581,
             1.5602, 1.5623, 1.5644, 1.5665, 1.5686, 1.5707, 1.5728, 1.5748, 1.5769, 1.5790, 1.5810, 1.5831, 1.5851,
             1.5872, 1.5892, 1.5913, 1.5933, 1.5953, 1.5974, 1.5994, 1.6014, 1.6034, 1.6054, 1.6074, 1.6094, 1.6114,
             1.6134, 1.6154, 1.6174, 1.6194, 1.6214, 1.6233, 1.6253, 1.6273, 1.6292, 1.6312, 1.6332, 1.6351, 1.6371,
             1.6390, 1.6409, 1.6429, 1.6448, 1.6467, 1.6487, 1.6506, 1.6525, 1.6544, 1.6563, 1.6582, 1.6601, 1.6620,
             1.6639, 1.6658, 1.6677, 1.6696, 1.6715, 1.6734, 1.6752, 1.6771, 1.6790, 1.6808, 1.6827, 1.6845, 1.6864,
             1.6882, 1.6901, 1.6919, 1.6938, 1.6956, 1.6974, 1.6993, 1.7011, 1.7029, 1.7047, 1.7066, 1.7084, 1.7102,
             1.7120, 1.7138, 1.7156, 1.7174, 1.7192, 1.7210, 1.7228, 1.7246, 1.7263, 1.7281, 1.7299, 1.7317, 1.7334,
             1.7352, 1.7370, 1.7387, 1.7405, 1.7422, 1.7440, 1.7457, 1.7475, 1.7492, 1.7509, 1.7527, 1.7544, 1.7561,
             1.7579, 1.7596, 1.7613, 1.7630, 1.7647, 1.7664, 1.7681, 1.7699, 1.7716, 1.7733, 1.7750, 1.7766, 1.7783,
             1.7800, 1.7817, 1.7834, 1.7851, 1.7867, 1.7884, 1.7901]

list_data3 = [885, 886, 899, 840, 830]
list_data4 = [0, 0, 0, 0, 0, 63, 126, 189, 0, 315, 378, 441, 504, 567, 630,
              652, 674, 696, 718, 740, 762, 784, 806, 828, 850,
              851.5, 853.0, 854.5, 856.0, 857.5, 859.0, 860.5, 862.0, 863.5,
              865, 866.1, 867.2, 868.3, 869.4, 870.5, 871.6, 872.7, 873.8, 874.9, 890,
              0, 0, 0, 0, 0, 836, 835, 834, 833, 832, 831, 830,
              829, 828, 827, 826, 825, 824, 823, 822, 821, 820,
              808, 796, 784, 772, 760, 748, 736, 724, 712, 700,
              690, 680, 670, 660, 650, 640, 630, 620, 610, 600]


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


class PaintArea(QWidget):
    def __init__(self):
        super(PaintArea, self).__init__()
        self.setWindowTitle("Main Window")
        self.resize(1760, 800)
        self.setMinimumSize(704, 320)
        # self.antialised = True
        self.clicked_point = QPoint(0, 0)
        self.state_clicktimes = 0
        self.clickedtimes = 0
        self.ori_w = 0
        self.ori_h = 0

        color_blue = QColor(110, 168, 210)
        color_green = QColor(33, 85, 100)
        color_pink = QColor(255, 224, 230)
        color_gray = QColor(170, 170, 174)
        color_cao = QColor(150, 185, 125)
        self.pen_func1 = QPen()
        self.pen_func1.setColor(color_blue)
        self.pen_func1.setWidth(3)

        self.pen_func2 = QPen()
        self.pen_func2.setColor(color_green)
        self.pen_func2.setWidth(3)

        self.pen_func3 = QPen()
        self.pen_func3.setColor(color_cao)
        self.pen_func3.setWidth(4)

        self.pen_axis = QPen()
        self.pen_axis.setColor(color_gray)
        self.pen_axis.setWidth(2)

        self.pen_refer = QPen()
        self.pen_refer.setStyle(Qt.DotLine)
        # self.pen_refer.setDashPattern([1, 2, 1, 2])
        self.pen_refer.setColor(color_gray)
        self.pen_refer.setWidth(2)

        self.pen_infor = QPen()
        self.pen_infor.setColor(Qt.black)
        self.pen_infor.setWidth(1)

    def paintEvent(self, event):
        self.w = self.size().width()
        self.h = self.size().height()
        qpainter = QPainter()
        # qpainter.begin(self)
        # 根据单击双击设置画笔颜色

        if self.state_clicktimes == 1:
            qpainter.begin(self)
            self.pen1 = QPen(Qt.red, 3)
            qpainter.setPen(self.pen1)
        elif self.state_clicktimes == 2:
            qpainter.begin(self)
            self.pen1 = QPen(Qt.green, 3)
        elif self.state_clicktimes == 0:
            qpainter.begin(self)
            self.pen1 = QPen(Qt.black, 3)
        qpainter.setPen(self.pen1)
        self.draw_whole(qpainter)
        # 结束绘制
        qpainter.end()

    def draw_whole(self, qp):
        wr = int((self.w - 30) / 2)  # func_rect 宽度width
        hr = int((self.h - 30) / 2)  # func_rect 高度height

        mouse_x = self.clicked_point.x()
        mouse_y = self.clicked_point.y()

        rect_blanc = self.rect()
        rect_blanc.setRect(10, 10, self.w - 20, self.h - 20)
        # print('mouse is here:', mouse_x, mouse_y)
        # print('w, h =', self.w, self.h)
        # print('draw background, the state_clicktimes =', self.state_clicktimes)
        # 根据鼠标点击后所在空间位置，进行比例放缩，以防止窗口大小导致绘制区域改变
        if (self.state_clicktimes == 1) or (self.state_clicktimes == 2):
            mouse_x = int((mouse_x / self.refresh_w) * self.w)
            mouse_y = int((mouse_y / self.refresh_h) * self.h)
        elif self.state_clicktimes == 0:
            # 未点击之前，显示白底黑框加“点击开始绘制”，以及分区
            qp.fillRect(rect_blanc, Qt.white)
            qp.setFont(QFont('', 15))
            qp.drawRoundedRect(rect_blanc, 10, 10)
            x_1 = int(self.w / 4)
            x_2 = int(3 * self.w / 4)
            y_1 = int(self.h / 4)
            y_2 = int(3 * self.h / 4)
            # qp.drawText(30, 20, 300, 50, 0, '申请编号:Q20210525 姓名:质控CK2')
            qp.drawText(x_1 - 45, y_1 - 12, 100, 100, 0, 'AREA 1')
            qp.drawText(x_2 - 45, y_1 - 12, 100, 100, 0, 'AREA 2')
            qp.drawText(x_1 - 45, y_2 - 12, 100, 100, 0, 'AREA 3')
            qp.drawText(x_2 - 45, y_2 - 12, 100, 100, 0, 'AREA 4')
            qp.setPen(self.pen_refer)
            qp.drawLine(12, 2 * y_1, self.w - 12, 2 * y_1)
            qp.drawLine(2 * x_1, 12, 2 * x_1, self.h - 12)

        # print('实时鼠标等比放缩位置:', mouse_x, mouse_y)
        # print('窗口实时大小:', self.w, self.h)

        rect1 = self.rect()
        rect1.setRect(10, 10, wr, hr)
        rect2 = self.rect()
        rect2.setRect(20 + wr, 10, wr, hr)
        rect3 = self.rect()
        rect3.setRect(10, 20 + hr, wr, hr)
        rect4 = self.rect()
        rect4.setRect(20 + wr, 20 + hr, wr, hr)
        # for fill_white in (rect1, rect2, rect3, rect4):
        #     qp.fillRect(fill_white, Qt.white)

        # 为保证所有函数依赖同一个坐标系，需要找出数据和数据量各自的最大值
        # 并根据数据和数据量的最大值，压缩/扩张数据到坐标轴上
        # 如果需要固定数值需要稍微改动
        l_list = [len(list_data), len(list_data2)]  # 用这个列表列出不同数据组的数据量
        m_list = [max(list_data), max(list_data2)]  # 用这个列表列出不同数据组最大的数
        self.trans_x = ((self.w - 90) / 2 - 100) / max(l_list)
        self.trans_y = ((self.h - 150) / 4) / max(m_list)
        if mouse_x != 0 and mouse_y != 0:
            for fill_white in (rect1, rect2, rect3, rect4):
                qp.fillRect(fill_white, Qt.white)
            if (mouse_x < self.w / 2) and (mouse_y < self.h / 2):
                qp.drawRoundedRect(rect1, 10, 10)
                self.draw_reference(qp, 1)
                self.draw_axis(qp, 1, wr, hr)
                self.draw_character(qp, 1)
            elif (mouse_x > self.w / 2) and (mouse_y < self.h / 2):
                qp.drawRoundedRect(rect2, 10, 10)
                self.draw_reference(qp, 2)
                self.draw_axis(qp, 2, wr, hr)
                self.draw_character(qp, 2)
            elif (mouse_x < self.w / 2) and (mouse_y > self.h / 2):
                qp.drawRoundedRect(rect3, 10, 10)
                self.draw_reference(qp, 3)
                self.draw_axis(qp, 3, wr, hr)
                self.draw_character(qp, 3)
            elif (mouse_x > self.w / 2) and (mouse_y > self.h / 2):
                qp.drawRoundedRect(rect4, 10, 10)
                self.draw_reference(qp, 4)
                self.draw_axis(qp, 4, wr, hr)
                self.draw_character(qp, 4)

        elif (mouse_x == 0) and (mouse_y == 0):
            print('没进来啊')

    def draw_axis(self, qp, square, wr, hr):
        qp.setPen(self.pen_axis)
        line1_r = int((self.w - 90) / 2 + 25)  # line1右端点水平坐标
        line1_h = int((self.h - 30) / 4 + 10)  # line1竖直坐标
        line2_l = line1_r + 40  # line2左端点水平坐标
        line2_r = self.w - 25  # line2右端点水平坐标
        line3_h = int(3 * (self.h - 30) / 4 + 20)  # line3竖直坐标
        upright_h = int((self.h - 110) / 2)  # 实线y轴长度，即函数绘制区域总高度
        if square == 1:
            qp.drawLine(25, line1_h, line1_r, line1_h)
            qp.drawLine(25, 30, 25, 30 + upright_h)
            qp.setPen(self.pen_func1)
            self.draw_function(qp, 1, line1_h, 'AA', 25, list_data)
            qp.setPen(self.pen_func2)
            self.draw_function(qp, 1, line1_h, 'A', 25, list_data2)
        elif square == 2:
            qp.drawLine(line2_l, line1_h, line2_r, line1_h)
            qp.drawLine(35 + wr, 30, 35 + wr, 30 + upright_h)
            qp.setPen(self.pen_func1)
            self.draw_function(qp, 2, line1_h, 'AA', line2_l, list_data)
            qp.setPen(self.pen_func2)
            self.draw_function(qp, 2, line1_h, 'A', line2_l, list_data2)
        elif square == 3:
            qp.drawLine(25, line3_h, line1_r, line3_h)
            qp.drawLine(25, 40 + hr, 25, 40 + hr + upright_h)
            qp.setPen(self.pen_func1)
            self.draw_function(qp, 3, line3_h, 'AA', 25, list_data)
            qp.setPen(self.pen_func2)
            self.draw_function(qp, 3, line3_h, 'A', 25, list_data2)
        elif square == 4:
            # todo: 在这里执行函数修复测试
            qp.drawLine(line2_l, line3_h, line2_r, line3_h)
            qp.drawLine(35 + wr, 40 + hr, 35 + wr, 40 + hr + upright_h)

            count = 0
            a = np.array(list_data4)
            # print('list_data4=', a)
            list_storage = a
            while count <= (len(list_data4) - 5):
                # print('count=', count)
                s = slice(count, count + 5, 1)
                count += 1
                b = a[s]
                k1 = b[1] - b[0]
                k2 = b[2] - b[1]
                k3 = b[3] - b[2]
                k4 = b[4] - b[3]
                # print('k=', k1, k2, k3, k4)
                state1 = 0  # 第三个点是否凸起或凹陷，0-否，1-是.
                state2 = 0  # 第三个点两侧斜率是否异常大，0-否，1-是.
                if k2 * k3 < 0:
                    # 第三个点凸起或凹陷
                    state1 = 1

                k1 = abs(k1)
                k2 = abs(k2)
                k3 = abs(k3)
                k4 = abs(k4)

                if (k2 + k3) > 3 * (k1 + k4) and (k3 != 0 and k4 != 0):
                    # 判断条件有：斜率异常大，后三点不是直线，均满足则确认
                    # print('第三个点两侧斜率异常大，count=', count-1)
                    state2 = 1

                if state1 == 1 and state2 == 1:
                    #  两个条件均满足，则执行修复
                    print("条件均满足判断，进行修复！！！")
                    list_storage[count + 1] = (b[1] + b[3]) / 2
                    # print('修复后list_storage=', list_storage)

            if self.state_clicktimes == 1:
                # qp.setPen(self.pen_func1)
                # self.draw_function(qp, 4, line3_h, 'AA', line2_l, list_data3)
                qp.setPen(self.pen_func2)
                self.draw_function(qp, 4, line3_h, 'A', line2_l, list_data4)
            elif self.state_clicktimes == 2:
                # qp.setPen(self.pen_func1)
                # self.draw_function(qp, 4, line3_h, 'AA', line2_l, list_data3)
                qp.setPen(self.pen_func3)
                self.draw_function(qp, 4, line3_h, 'X', line2_l, list_storage)

    def draw_character(self, qp, square):

        qp.setFont(QFont('方正FW筑紫A圆 简 D', 20))
        if square == 1:
            qp.drawText(100, 100, 150, 100, 0, 'AREA Ⅰ')
            qp.setFont(QFont('', 10))
            qp.setPen(Qt.gray)
            qp.drawText(30, 20, 300, 50, 0, '申请编号:Q20210525 姓名:质控CK2')
        elif square == 2:
            qp.drawText(int(100 + (self.w - 30) / 2), 100, 150, 100, 0, 'AREA Ⅱ')
        elif square == 3:
            qp.drawText(100, int(100 + (self.h - 30) / 2), 150, 100, 0, 'AREA Ⅲ')
        elif square == 4:
            qp.drawText(int(100 + (self.w - 30) / 2), int(100 + (self.h - 30) / 2), 150, 100, 0, 'AREA Ⅳ')

    def draw_function(self, qp, square, a, b, c, data):
        # a为Ⅰ、Ⅱ区横坐标轴的纵坐标 b为函数图像曲线的名称
        step = 0
        # print('传递参数T =', self.trans_y, type(self.trans_y))
        final_xs = 0
        final_ys = 0
        while step <= len(data) - 2:
            if square == 4:
                self.trans_x = ((self.w - 90) / 2 - 100) / len(list_data4)
                self.trans_y = ((self.h - 150) / 4) / 1000
            final_ys = int(data[step] * self.trans_y)  # 起始点最终绘制离轴距离
            final_ye = int(data[step + 1] * self.trans_y)  # 尾端点最终绘制离轴距离
            final_xs = int(step * self.trans_x)  # 起始点x轴坐标
            final_xe = int((step + 1) * self.trans_x)  # 尾端点x轴坐标
            s_point = QPoint(c + final_xs, a + final_ys)
            e_point = QPoint(c + final_xe, a + final_ye)
            mirror_s = QPoint(c + final_xs, a - final_ys)  # 镜像点
            mirror_e = QPoint(c + final_xe, a - final_ye)
            qp.drawLine(s_point, e_point)
            qp.drawLine(mirror_s, mirror_e)
            step += 1
        qp.setFont(QFont('', 15))
        qp.drawText(c + 10 + final_xs, a - 10 - final_ys, 50, 50, 0, b)
        qp.drawText(c + 10 + final_xs, a - 10 + final_ys, 50, 50, 0, b)

    def draw_reference(self, qp, square):
        qp.setPen(self.pen_refer)
        m1 = '%.2f' % max(list_data)
        m2 = '%.2f' % max(list_data2)
        tran_rw = ((self.w - 90) - 200) / ((self.ori_w - 90) - 200)  # 参考线位置收缩
        tran_rh = (self.h - 90) / (self.ori_h - 90)
        # 为了便于理解，这里之间通过计算给出相邻两条参考线之间的距离大小distance_v (Vertical) & ditance_h (Horizontal)
        distance_h = int((self.ori_h - 90) / 16)
        distance_v = int(((self.ori_w - 90) / 2 - 100) / 5)  # (self.w - 90) / 2 - 100)
        for i in (distance_v, 2 * distance_v, 3 * distance_v, 4 * distance_v, 5 * distance_v):
            h = int((self.h - 90) / 2)  # 参考线长
            incre = 0
            r = 0
            if (self.state_clicktimes == 1) or (self.state_clicktimes == 2):
                r1 = 25 + int(i * tran_rw)
                r2 = 35 + int((self.w - 30) / 2 + i * tran_rw)
                if (square == 1) or (square == 3):
                    r = r1
                elif (square == 2) or (square == 4):
                    r = r2
                # --- #
                if (square == 3) or (square == 4):
                    incre = h + 40
                qp.drawLine(r, 25 + incre, r, 25 + h + incre)
        for i in (distance_h, 2 * distance_h, 3 * distance_h, 4 * distance_h):
            base = 0
            base_x = 0
            base1 = int((self.h - 30) / 4 + 10)
            base2 = int(self.h - (self.h - 30) / 4 - 10)
            long = int((self.w - 90) / 2)
            if (square == 1) or (square == 2):
                base = base1
            elif (square == 3) or (square == 4):
                base = base2
            if (square == 2) or (square == 4):
                base_x = 10 + int((self.w - 30) / 2)
            qp.drawLine(25 + base_x, base + int(i * tran_rh), 25 + long + base_x, base + int(i * tran_rh))
            qp.drawLine(25 + base_x, base - int(i * tran_rh), 25 + long + base_x, base - int(i * tran_rh))
            if i == 4 * distance_h:
                qp.setPen(self.pen_infor)
                qp.setFont(QFont('方正FW筑紫A圆 简 D', 14))
                qp.drawText(35 + base_x, base + int(i * tran_rh) - 45, 450, 80, 0, '   A:\nAA:')
                qp.drawText(90 + base_x, base + int(i * tran_rh) - 45, 450, 80, 0, m2 + '\n' + m1)

    def mousePressEvent(self, event):
        self.clickedtimes += 1
        if self.clickedtimes == 1:
            self.ori_w = self.size().width()
            self.ori_h = self.size().height()

        self.state_clicktimes = 1
        self.pressX = event.x()  # 记录鼠标按下的时候的坐标
        self.pressY = event.y()
        self.clicked_point = event.pos()
        self.refresh_w = self.size().width()
        self.refresh_h = self.size().height()
        print('mouse clicked here:', event.x(), event.y())
        print('Now draw area size:', self.w, self.h)
        print('Original size:', self.ori_w, self.ori_h)
        self.update()

    def mouseDoubleClickEvent(self, event):
        self.state_clicktimes = 2
        self.clicked_point = event.pos()
        self.update()


class DataRepair(QWidget):
    def __init__(self):
        super(DataRepair, self).__init__()
        self.setWindowTitle('Abnormal Data Repair')
        self.resize(880, 480)

        # self.plotlib=
        # todo: matplotlib模块不能正常加载，暂时不处理这个了。。。
        self.data_input = QLineEdit('')
        self.data_location = QComboBox()
        self.data_location.addItem('1')
        self.data_location.addItem('2')
        self.data_location.addItem('3')
        self.data_location.addItem('4')
        self.data_location.addItem('5')

        self.change_button = QPushButton('Change!')
        self.change_button.clicked.connect(self.change_data)

        self.initUI()

    def initUI(self):
        wl = QVBoxLayout()
        h1 = QHBoxLayout()
        h1.addWidget(self.data_input)
        h1.addWidget(self.data_location)
        h1.addWidget(self.change_button)
        # wl.addWidget
        wl.addLayout(h1)

        main_frame = QWidget()
        main_frame.setLayout(wl)
        self.setLayout(wl)

    def change_data(self):
        print("change!")


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
        data_bar = QAction(QIcon('./icon/paint_icon.jpg'), "Data Repair", self)
        self.toolbar3.addAction(close_bar)
        self.toolbar3.addAction(data_bar)
        self.toolbar3.setMovable(False)
        self.toolbar3.actionTriggered[QAction].connect(self.toolbtnpressed)

        # self.create_toolbar = QAction()

    def toolbtnpressed(self, a):
        print("Push the toolbar button:", a.text())
        if a.text() == "Table":
            self.open_table()
        elif a.text() == "Paint":
            self.paint_sth()
        elif a.text() == "Data Repair":
            print('开始数据修复模块')
            self.data_re()

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
        self.p_d = PaintArea()
        self.p_d.show()

    def data_re(self):
        self.re_data = DataRepair()
        self.re_data.show()

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
