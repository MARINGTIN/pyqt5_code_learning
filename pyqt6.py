"""
2021-11-04
1.) 鼠标点击屏幕，获取坐标；
2.) 将屏幕以 ‘田’ 字型分割（不显示），并且根据鼠标所在区域画出所在1/4区域
3.) 根据单、双击设置该区域色彩
"""
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.Qt import *
import sys


class Main_Win(QWidget):
    def __init__(self):
        super(Main_Win, self).__init__()
        self.setWindowTitle("Main Window")
        self.resize(1600, 800)
        self.clicked_point = QPoint(800, 400)
        self.state_clicktimes = 1

        '''           1600
         -------------------------------
        |       10              10      |  ^
        | 1 ---------  10   ---------   |  |
        | 0|    ①    | 10 |   ②     |1 |  |
        |   ---------  10   --------- 0 |  800
        |       10            10        |
        |     
        |      ③              ④
        '''

    def paintEvent(self, event):
        qpainter = QPainter()
        qpainter.begin(self)
        self.draw_roundedrect(qpainter)
        qpainter.end()

    def draw_roundedrect(self, qp):

        if self.state_clicktimes == 1:


            qp.setPen(Qt.red)
        elif self.state_clicktimes == 2:
            qp.setPen(Qt.green)
        w = self.size().width()
        h = self.size().height()
        wr = int((w - 30) / 2)
        hr = int((h - 30) / 2)

        mouse_x = self.clicked_point.x()
        mouse_y = self.clicked_point.y()
        print('test paint', self.clicked_point)

        # if (mouse_x < w/2 | mouse_y < h/2):

        rect1 = self.rect()
        rect1.setRect(10, 10, wr, hr)
        rect2 = self.rect()
        rect2.setRect(20 + wr, 10, wr, hr)
        rect3 = self.rect()
        rect3.setRect(10, 20 + hr, wr, hr)
        rect4 = self.rect()
        rect4.setRect(20 + wr, 20 + hr, wr, hr)

        # qp.drawRoundedRect(rect1, 10, 10)
        # qp.drawRoundedRect(rect2, 10, 10)
        # qp.drawRoundedRect(rect3, 10, 10)
        # qp.drawRoundedRect(rect4, 10, 10)

        if (mouse_x < w / 2) and (mouse_y < h / 2):
            qp.drawRoundedRect(rect1, 10, 10)
        elif (mouse_x < w / 2) and (mouse_y > h / 2):
            qp.drawRoundedRect(rect3, 10, 10)
        elif (mouse_x > w / 2) and (mouse_y < h / 2):
            qp.drawRoundedRect(rect2, 10, 10)
        elif (mouse_x > w / 2) and (mouse_y > h / 2):
            qp.drawRoundedRect(rect4, 10, 10)

    def mousePressEvent(self, event):
        self.state_clicktimes = 1
        self.pressX = event.x()  # 记录鼠标按下的时候的坐标
        self.pressY = event.y()
        self.clicked_point = event.pos()
        print('mouse is here: ', self.pressX, self.pressY)
        # pw = Paint_Win()
        # self.last
        self.update()

    def mouseDoubleClickEvent(self, event):
        self.state_clicktimes = 2
        self.clicked_point = event.pos()
        self.update()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main_Win()
    main.show()
    sys.exit(app.exec_())
