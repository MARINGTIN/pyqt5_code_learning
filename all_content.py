class Text_Content:
    def __init__(self):
        # text content
        self.con1_en = "Username:"
        self.con1_cn = "用户名: "

        self.con3_en = "Select the Language"
        self.con3_cn = "选择你想要的语言"
        self.con4_en = 'The Password which you entre\nwill pass into first windows\' text box\n\nPlease entre here: '
        self.con4_cn = "在本页面输入的密码\n将会在确认后传回主窗口的密码栏\n\n在下方输入："
        # text on the button
        self.btn1_en = "Clear"
        self.btn1_cn = "清除"
        self.btn2_en = "Close"
        self.btn2_cn = "关闭"
        self.btn3_en = " Password "
        self.btn3_cn = "  密  码  "
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
        # text of the checkbox
        self.agq_en = "Please read the following user agreements carefully:"
        self.agq_cn = "请仔细阅读以下用户协议："
        self.agt_en = "Please confirm that you are aware that the results of using this service and the associated " \
                      "information generated therefrom will be stored.\nIf you are aware of the risk of information " \
                      "leakage caused by this service and insist on using this service, please check the two " \
                      "Checkboxes below and click Next.\nIf you reject this service regulation, please choose to " \
                      "cancel, and the information will be completely destroyed after the end of this service.\nOf " \
                      "course, you have to accept and bear the related risks and continue to use this service. "
        self.agt_cn = "请确认您已经知悉使用本服务的结果和因此产生的关联信息将被存储。\n如果您已经知悉了本服务" \
                      "所带来的信息泄露风险，并坚持使用本服务，请确认选择下方的同意按钮，并点击下一步。\n" \
                      "如果您拒绝本服务，请选择取消，本次服务结束后信息也将彻底销毁。\n" \
                      "当然您不能不接受并承担相关的风险还继续使用本服务。"
        self.qr1_en = "I accept the above agreement and voluntarily assume all risks."
        self.qr1_cn = "我已阅读上述文本内容，已经知悉其中风险。我确认接受以上协议，并自愿承担全部风险。"
        self.qr2_en = "I refuse to accept the above agreement."
        self.qr2_cn = "我拒绝接受以上协议。"

        '''我有个程序简化的想法，把这些都装进字典（或者列表或者元组随便啥都行），然后在中英文切换的时候只需要写个循环让所有元素加减1就行'''
        self.con_lib = ["Enter username:", "输入用户名:   ", "Select the Language", "选择你想要的语言",
                        'The Password which you entre\nwill pass into first windows\' text box\n\n',
                        "在本页面输入的密码\n将会在确认后传回主窗口的密码栏\n\n在下方输入：", "Clear", "清除", "Close", "关闭",
                        " Password ", "  密  码  ", " Get  age ", " 获取年龄 ", "Register", "登记", "Tree(Test)",
                        "数据树（测试）", "File", "文件(F)", "Edit", "编辑(&E)", "View", "视图(&V)", "Warning!", "警告！",
                        "Check Username, Password & Age,\nthere is blanc among them.",
                        "请检查输入的用户名，密码或年龄，\n其中有空白项，本次数据将不会导入"]
