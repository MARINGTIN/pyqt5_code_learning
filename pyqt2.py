import sys, math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Draw_Window(QWidget):
    def __init__(self):
        super(Draw_Window, self).__init__()
        self.resize(300, 200)
        self.setWindowTitle('Drawing')
        for i in range(100000000):
            print(i)


    def paintEvent(self, event):
        a = self.size()
        w = a.width()
        h = a.height()
        print(w, h,type(w))
        qp = QPainter()
        qp.begin(self)
        self.drawPoints(qp)
        qp.end()

    def drawPoints(self, qp):
        qp.setPen(Qt.red)
        size = self.size()
        self.adjustSize()

        for i in range(1000):
            # 绘制正弦函数图像，它的周期是【-100,100】
            x = 100 * (-1 + 2.0 * i / 1000) + size.width() / 2.0
            y = -50 * math.sin((x - size.width() / 2.0) * math.pi / 50) + size.height() / 2.0
            # n = i/1000
            # m = size.width()/2.0

            qp.drawPoint(x, y)
            # qp.drawPoints(n, m)

if __name__ == '__main__':
        app = QApplication(sys.argv)
        demo = Draw_Window()
        demo.show()
        sys.exit(app.exec_())
