import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, qApp, QMenu
from PyQt5.QtGui import QIcon, QStatusTipEvent


class main_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 可以设置 动作的图标， 文字显示； 强大
        exitAct = QAction(QIcon("/Users/zuozhe/PycharmProjects/Soft-Video/images/m4.png"), "&退出", self)
        exitAct.setShortcut("Ctrl+Q")  # 设置快捷键
        exitAct.setToolTip("Exit Application")  # 提示
        exitAct.triggered.connect(qApp.exit)  # 绑定退出事件

        status = self.statusBar()  # 创建状态栏
        status.showMessage("ready!")  # 显示消息

        # 菜单栏
        # 文件菜单栏
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)  # MAC OS 下需要设置此句话
        fileMenu = menubar.addMenu("&File")  # 主菜单File

        impMenu = QMenu("Import", self)  # 创建菜单项
        impAct = QAction("Import Email", self)  # Import菜单下有子菜单 Import Email
        impMenu.addAction(impAct)

        newAct = QAction("New", self)
        # 就差 给 Action(动作)绑定触发事件了
        fileMenu.addAction(newAct)  # 将两个菜单项加入到 File主菜单栏下
        fileMenu.addMenu(impMenu)
        fileMenu.addAction(exitAct)  # 绑定 File下的菜单项
        # 编辑菜单栏
        editMenu = menubar.addMenu("&Edit")

        # 视图菜单栏
        viewMenu = menubar.addMenu("&View")
        # 勾选菜单
        viewstatAct = QAction("是否显示状态栏", self, checkable=True)
        viewstatAct.setToolTip("View statusbar")
        viewstatAct.setChecked(True)
        viewstatAct.triggered.connect(self.toggleMenu)  # 触发链接事件; toggleMenu是自定义函数
        viewMenu.addAction(viewstatAct)

        # 设置窗口的 位置和大小
        self.setGeometry(300, 300, 500, 600)
        self.setWindowTitle("主窗口的菜单栏和工具栏")
        self.show()

    # 此覆盖父类函数: 覆盖方法； 为了克服 将鼠标放置于菜单栏上 状态栏就消失的问题；
    def event(self, QEvent):
        if QEvent.type() == QEvent.StatusTip:
            if QEvent.tip() == "":
                QEvent = QStatusTipEvent("ready!")  # 此处为要始终显示的内容
        return super().event(QEvent)

    def toggleMenu(self, state):  # 自定义事件函数
        print(state)
        # if state:
        #     self.statusBar().showMessage("ready!")
        # else:
        #     self.statusBar().showMessage("")
        # if state:  # 控制状态栏是否显示,
        #     self.statusbar().show()
        # else:
        #     self.statusbar().hide()

        if state:  # 应该使用statusBar() 而不是 statusbar
            self.statusBar().show()
        else:
            self.statusBar().hide()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = main_window()
    sys.exit(app.exec_())
