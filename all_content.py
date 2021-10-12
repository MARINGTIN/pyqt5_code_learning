class Text_Content:
    def __init__(self):
        # text content
        self.con1_en = "Enter username:"
        self.con1_cn = "输入用户名:   "

        self.con3_en = "Select the Language"
        self.con3_cn = "选择你想要的语言"
        self.con4_en = 'The Password which you entre\nwill pass into first windows\' text box\n\nPlease entre here: '
        self.con4_cn = "在本页面输入的密码\n将会在确认后传回主窗口的密码栏\n\n在下方输入："
        # text on the button
        self.btn1_en = "Clear"
        self.btn1_cn = "清除"
        self.btn2_en = "Close"
        self.btn2_cn = "关闭"
        self.btn3_en = "Password"
        self.btn3_cn = "  密      码  "
        self.btn4_en = " Get  age "
        self.btn4_cn = " 获取年龄 "
        self.btn5_en = " Register "
        self.btn5_cn = "登记"
        self.btn6_en = "Tree(Test)"
        self.btn6_cn = "数据树（测试）"
        # text of the menu
        self.str_menu1 = ["File", "文件(F)"]
        self.str_menu2 = ["Edit", "编辑(&E)"]
        self.str_menu3 = ["View", "视图(&V)"]
        # text of the message box
        self.mes1_en = "Warning!"  # title
        self.mes1_cn = "警告！"
        self.mes2_en = "Check Username, Password & Age,\nthere is blanc among them."
        self.mes2_cn = "请检查输入的用户名，密码或年龄，\n其中有空白项，本次数据将不会导入"

        '''我有个程序简化的想法，把这些都装进字典（或者列表或者元组随便啥都行），然后在中英文切换的时候只需要写个循环让所有元素加减1就行'''
        self.con_lib = ["Enter username:", "输入用户名:   ", "Select the Language", "选择你想要的语言",
                        'The Password which you entre\nwill pass into first windows\' text box\n\n',
                        "在本页面输入的密码\n将会在确认后传回主窗口的密码栏\n\n在下方输入：", "Clear", "清除", "Close", "关闭",
                        " Password ", "  密  码  ", " Get  age ", " 获取年龄 ", "Register", "登记", "Tree(Test)",
                        "数据树（测试）", "File", "文件(F)", "Edit", "编辑(&E)", "View", "视图(&V)", "Warning!", "警告！",
                        "Check Username, Password & Age,\nthere is blanc among them.",
                        "请检查输入的用户名，密码或年龄，\n其中有空白项，本次数据将不会导入"]
