"""
本文件将实现用户登录的功能，以pyqt1的内容为基础
1.) 需要设立admin超级管理员以管理用户，pyqt1的内容正是为此设计的
2.) 设立登录窗口(Log_In)，用户检测(User_Match)，超级管理员账户(Admin)
3.) ...
"""
import sys
import re
import time

from all_content import *  # all content
from PyQt5.Qt import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


# These are all the font types which i will need.
class Font_Type:
    def __init__(self):
        super(Font_Type, self).__init__()
        self.font_1 = QFont(QFont().defaultFamily(), 12)
        font_t1 = QFont("方正FW筑紫A圆 简 D", 14)
        self.font_2 = QFont(font_t1)


class Log_In(QWidget):
    def __init__(self):
        super(Log_In, self).__init__()
        ft = Font_Type()
        self.resize(540, 420)
        self.setWindowTitle("登录界面")
        self.setWindowModality(Qt.ApplicationModal)  # 打开该界面，将阻止你使用Main_Window
        self.setWindowFlags(Qt.FramelessWindowHint)  # 消除窗口标题栏
        self.setFixedSize(self.width(), self.height())  # 用于禁止改变窗口大小
        palette = QPalette()  # insert the background image
        palette.setBrush(QPalette.Background, QBrush(QPixmap("./icon/background.png")))
        self.setPalette(palette)

        self.m_conut = 0  # 计数（mouseMoveEvent)

        action1 = QAction(self)
        action2 = QAction(self)
        # action3 = QAction(self)
        action1.setIcon(QIcon('./icon/user.png'))
        action2.setIcon(QIcon('./icon/lock.png'))
        # action3.setIcon(QIcon('./icon/X.png'))

        self.box_username = QLineEdit()
        self.box_username.setClearButtonEnabled(True)
        self.box_username.addAction(action1, QLineEdit.LeadingPosition)  # insert the image
        self.box_password = QLineEdit()
        self.box_password.setClearButtonEnabled(True)
        self.box_password.addAction(action2, QLineEdit.LeadingPosition)
        self.box_password.setEchoMode(QLineEdit.Password)

        self.button_log = QPushButton("登录")
        self.button_log.clicked.connect(self.log_in)
        self.button_can = QPushButton("取消")
        self.button_can.clicked.connect(self.can)

        for sT in (self.box_password, self.box_username, self.button_can, self.button_log):
            sT.setFont(ft.font_2)
            sT.setStyle(QStyleFactory.create("Fusion"))
            sT.setMinimumSize(310, 40)

        self.button_X = QPushButton()
        self.button_X.setMaximumWidth(37)
        self.button_X.clicked.connect(self.can)
        self.button_X.setIcon(QIcon('./icon/X.png'))
        self.button_X.setIconSize(QSize(37, 37))
        self.button_X.setStyleSheet('QPushButton{background-color: rgba(0, 0, 0, 0); border-radius: 5px}'
                                    'QPushButton:hover{background-color: rgba(255, 255, 255, 100); border-radius: 5px}'
                                    'QPushButton:pressed{background-color: rgb(255, 255, 255, 200);'
                                    'border-radius: 5px}')

        self.initUI()

    def initUI(self):
        wl = QVBoxLayout(self)
        h1 = QVBoxLayout()
        h2 = QVBoxLayout()
        h3 = QVBoxLayout()

        for box_all in (self.box_username, self.box_password, self.button_log, self.button_can):
            h2.addWidget(box_all, 0, Qt.AlignHCenter)
        wl.addWidget(self.button_X)
        wl.addStretch(10)
        wl.addLayout(h2)
        wl.addStretch(1)
        self.setLayout(wl)

    def log_in(self):
        str_username = self.box_username.text()
        str_password = self.box_password.text()
        print('click Log_In,\nusername:', str_username, ' | password:', str_password, type(str_username))

    def can(self):
        print('Close after 0.5s!')
        time.sleep(0.3)
        self.close()

    def mousePressEvent(self, event):
        self.pressX = event.x()  # 记录鼠标按下的时候的坐标
        self.pressY = event.y()

    def mouseMoveEvent(self, event):
        x = event.x()
        y = event.y()  # 获取移动后的坐标
        moveX = x - self.pressX
        moveY = y - self.pressY  # 计算移动了多少
        positionX = self.frameGeometry().x() + moveX
        positionY = self.frameGeometry().y() + moveY  # 计算移动后主窗口在桌面的位置
        self.move(positionX, positionY)  # 移动主窗口
        print(self.m_conut)
        self.m_conut += 1


class Main_Window(QMainWindow):
    def __init__(self):
        super(Main_Window, self).__init__()
        self.setWindowTitle("主界面")
        self.resize(450, 220)
        self.setFixedSize(self.width(), self.height())
        self.button_ol = QPushButton("Log In")
        self.button_ol.clicked.connect(self.btn_ol)
        self.button_tt = QPushButton("TEST")
        self.button_tt.clicked.connect(self.test_int)

        self.int_test = QLineEdit()
        test_validator = QIntValidator(self)
        test_validator.setRange(-1600, 255)
        self.int_test.setValidator(test_validator)
        self.b = self.int_test.validator()

        # cc = self.int_test.text()
        # self.b = test_validator.validate(cc, 0)

        self.initUI()
        '''
        screen = QDesktopWidget().screenGeometry()
        print(screen.width(), screen.height())
        '''

    # def MyValidator.QIntValidator()

    def initUI(self):
        wl = QVBoxLayout(self)
        h1 = QHBoxLayout()
        h1.addWidget(self.button_ol, 0, Qt.AlignCenter)
        h2 = QHBoxLayout()
        h2.addWidget(self.int_test)
        h2.addWidget(self.button_tt)
        wl.addLayout(h1)
        wl.addLayout(h2)
        main_lay = QWidget()
        main_lay.setLayout(wl)
        self.setCentralWidget(main_lay)
        self.show()

    def btn_ol(self):
        self.l_i = Log_In()
        self.l_i.show()

    def test_int(self):
        a = self.int_test.text()

        print(a, type(a))
        print(self.b, type(self.b))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    content = Text_Content()
    main = Main_Window()
    main.show()
    sys.exit(app.exec_())
