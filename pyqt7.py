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


class PaintArea(QWidget):
    def __init__(self):
        super(PaintArea, self).__init__()
        self.setWindowTitle("Main Window")
        self.resize(1760, 800)
        self.setMinimumSize(704, 320)
        self.clicked_point = QPoint(800, 400)
        self.state_clicktimes = 0

        self.ori_w = self.size().width()  # 原始宽度
        self.ori_h = self.size().height()  # 原始高度
        color_blue = QColor(110, 168, 210)
        color_green = QColor(33, 85, 100)
        color_pink = QColor(255, 224, 230)
        color_gray = QColor(170, 170, 174)
        self.pen_func1 = QPen()
        self.pen_func1.setColor(color_blue)
        self.pen_func1.setWidth(3)

        self.pen_func2 = QPen()
        self.pen_func2.setColor(color_green)
        self.pen_func2.setWidth(3)
        # self.pen_func3 = QPen()
        self.pen_axis = QPen()
        self.pen_axis.setColor(color_gray)
        self.pen_axis.setWidth(2)

        self.pen_refer = QPen()
        self.pen_refer.setStyle(Qt.CustomDashLine)
        self.pen_refer.setDashPattern([1, 2, 1, 2])
        self.pen_refer.setColor(color_gray)
        self.pen_refer.setWidth(2)

        self.pen_infor = QPen()
        self.pen_infor.setColor(Qt.black)
        self.pen_infor.setWidth(1)

        '''         
         -------------------------------
        |       10              10      |  
        | 1 ---------       ---------   |  
        | 0| |- ①   | 10  |  ②      |1 | 
        |   ---------       --------- 0 |  
        |       10            10        |
        |    ---------      ---------   |
        |   |    ③    |   |    ④    |  | 
        |    ---------      ---------   |  
         -------------------------------                 
        '''

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
            self.pen1 = QPen(Qt.black, 3)
        qpainter.setPen(self.pen1)
        self.draw_whole(qpainter)
        # 结束绘制
        qpainter.end()

    def draw_whole(self, qp):
        wr = int((self.w - 30) / 2)  # rect 宽度width
        hr = int((self.h - 30) / 2)  # rect 高度height

        mouse_x = self.clicked_point.x()
        mouse_y = self.clicked_point.y()
        # 根据鼠标点击后所在空间位置，进行比例放缩，以防止窗口大小导致绘制区域改变
        if (self.state_clicktimes == 1) or (self.state_clicktimes == 2):
            mouse_x = int((mouse_x / self.refresh_w) * self.w)
            mouse_y = int((mouse_y / self.refresh_h) * self.h)
        print('实时鼠标等比放缩位置:', mouse_x, mouse_y)
        print('窗口实时大小:', self.w, self.h)

        rect1 = self.rect()
        rect1.setRect(10, 10, wr, hr)
        rect2 = self.rect()
        rect2.setRect(20 + wr, 10, wr, hr)
        rect3 = self.rect()
        rect3.setRect(10, 20 + hr, wr, hr)
        rect4 = self.rect()
        rect4.setRect(20 + wr, 20 + hr, wr, hr)
        for fill_white in (rect1, rect2, rect3, rect4):
            qp.fillRect(fill_white, Qt.white)

        # 为保证所有函数依赖同一个坐标系，需要找出数据和数据量各自的最大值
        # 并根据数据和数据量的最大值，压缩/扩张数据到坐标轴上
        # 如果需要固定数值需要稍微改动
        l_list = [len(list_data), len(list_data2)]  # 用这个列表列出不同数据组的数据量
        m_list = [max(list_data), max(list_data2)]  # 用这个列表列出不同数据组最大的数
        self.trans_x = ((self.w - 90) / 2 - 100) / max(l_list)
        self.trans_y = ((self.h - 150) / 4) / max(m_list)

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

    def draw_axis(self, qp, square, wr, hr):
        qp.setPen(self.pen_axis)
        line1_r = int((self.w - 90) / 2 + 25)  # line1右端点水平坐标
        line1_h = int((self.h - 30) / 4 + 10)  # line1竖直坐标
        line2_l = line1_r + 40  # line2左端点水平坐标
        line2_r = self.w - 25  # line2右端点水平坐标
        line3_h = int(3 * (self.h - 30) / 4 + 20)  # line3竖直坐标
        upright_h = int((self.h - 110) / 2)  # y轴长度，即函数绘制区域总高度
        # print('AREA:', square, ' 绘制区域竖直全高度：', upright_h)
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
            qp.drawLine(line2_l, line3_h, line2_r, line3_h)
            qp.drawLine(35 + wr, 40 + hr, 35 + wr, 40 + hr + upright_h)
            qp.setPen(self.pen_func1)
            self.draw_function(qp, 4, line3_h, 'AA', line2_l, list_data)
            qp.setPen(self.pen_func2)
            self.draw_function(qp, 4, line3_h, 'A', line2_l, list_data2)

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
        # 五条参考线，150等分  (self.w - 90) / 2
        # i = 150
        # print('test, self.w, self.ori_w:', self.w, self.ori_w)
        tran_rw = (self.w - 90) / (self.ori_w - 90)  # 参考线位置收缩
        tran_rh = (self.h - 150) / (self.ori_h - 150)
        for i in (150, 300, 450, 600, 750):
            h = int((self.h - 50) / 2)  # 参考线长
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
                    incre = h + 20
                qp.drawLine(r, 15 + incre, r, 15 + h + incre)
        for i in (42, 84, 126, 168):
            base = 0
            base_x = 0
            base1 = int((self.h - 30) / 4 + 10)
            base2 = int(self.h-(self.h-30)/4-10)
            long = int((self.w - 90) / 2)
            if (square == 1) or (square == 2):
                base = base1
            elif (square == 3) or (square == 4):
                base = base2
            if (square == 2) or (square == 4):
                base_x = 10 + int((self.w - 30) / 2)
            qp.drawLine(25 + base_x, base + int(i * tran_rh), 25 + long + base_x, base + int(i * tran_rh))
            qp.drawLine(25 + base_x, base - int(i * tran_rh), 25 + long + base_x, base - int(i * tran_rh))
            if i == 168:
                qp.setPen(self.pen_infor)
                qp.setFont(QFont('方正FW筑紫A圆 简 D', 14))
                qp.drawText(35 + base_x, base + int(i * tran_rh) - 45, 450, 80, 0, '   A:\nAA:')
                qp.drawText(90 + base_x, base + int(i * tran_rh) - 45, 450, 80, 0, m2 + '\n' + m1)


    def mousePressEvent(self, event):
        self.state_clicktimes = 1
        self.pressX = event.x()  # 记录鼠标按下的时候的坐标
        self.pressY = event.y()
        self.clicked_point = event.pos()
        self.refresh_w = self.size().width()
        self.refresh_h = self.size().height()
        print('mouse clicked here: ', self.pressX, self.pressY)
        self.update()

    def mouseDoubleClickEvent(self, event):
        self.state_clicktimes = 2
        self.clicked_point = event.pos()
        self.update()


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
        paint = PaintArea()
        # splitter2.addWidget()
        # splitter2.addWidget(paint)
        splitter4 = QSplitter()
        splitter5 = QSplitter()
        splitter4.addWidget(textedit_2)
        splitter5.addWidget(paint)

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
