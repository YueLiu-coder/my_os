# 导入所需要的python包
import sys
from functools import partial
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
sys.dont_write_bytecode = True
import time
now = 0
global data
data = 0

# UI主窗口
class Ui_MainWindow(object):
    # 建立UI
    def setupUi(self, MainWindow):
        # 设置名字
        MainWindow.setObjectName("内存管理")
        # 控制窗口的大小
        MainWindow.resize(600, 350)
        # 设置style
        MainWindow.setStyleSheet("background-color: rgb(250, 250, 250);")

        # 添加菜单——模式按钮：可选首次适应算法或最佳适应算法
        self.menu_bar = QMainWindow.menuBar(MainWindow)
        self.model_bar = self.menu_bar.addMenu("动态分配策略")
        # 设置字体
        self.menu_bar.setFont(QtGui.QFont('Microsoft YaHei', 9))
        # 设置style
        self.menu_bar.setStyleSheet(
            "QMenuBar::item { \
                color: rgb(255,255,255);  /*字体颜色*/ \
                border: 2px solid rgb(120,120,120); \
                background-color:rgb(124,179,66);\
            } \
            QMenuBar::item:selected { \
                border: 2px solid rgb(66,66,66); \
                background-color:rgb(51,105,30);/*选中的样式*/ \
            } \
            QMenuBar::item:pressed {/*菜单项按下效果*/ \
                border: 2px solid rgb(66,66,66); \
                background-color: rgb(51,105,30); \
            }")


        # 向QMenu小控件中添加按钮，子菜单


        #首次适应算法按钮
        self.firstFit_bar = QtWidgets.QWidgetAction(MainWindow, checkable=True)
        # 设置被选中为True
        self.firstFit_bar.setChecked(True)
        # 设置标签
        self.firstFit_action = QtWidgets.QLabel(" √  First fit  ")
        # 设置字体
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        # 设置字体
        self.firstFit_action.setFont(font)
        # 设置style
        self.firstFit_action.setStyleSheet(
            "QLabel { color: rgb(255,255,255);  /*字体颜色*/ \
                background-color:rgb(51,105,30);\
                }"
            "QLabel:hover{  background-color:rgb(51,105,30);/*选中的样式*/ \
                }"
        )
        # 建立页面
        self.firstFit_bar.setDefaultWidget(self.firstFit_action)


        #最佳适应算法按钮
        self.bestFit_bar = QtWidgets.QWidgetAction(MainWindow, checkable=True)
        # 设置被选中为False
        self.bestFit_bar.setChecked(False)
        # 设置标签
        self.bestFit_action = QtWidgets.QLabel("     Best fit  ")
        # 设置字体
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        # 设置字体
        self.bestFit_action.setFont(font)
        # 设置style
        self.bestFit_action.setStyleSheet(
            "QLabel { color: rgb(225,225,225);  /*字体颜色*/ \
                background-color:rgb(124,179,66);\
                }"
            "QLabel:hover{ background-color:rgb(51,105,30);/*选中的样式*/ \
                            }"
        )
        # 建立页面
        self.bestFit_bar.setDefaultWidget(self.bestFit_action)


        # 最差适应算法按钮
        self.worseFit_bar = QtWidgets.QWidgetAction(MainWindow, checkable=True)
        # 设置被选中为False
        self.worseFit_bar.setChecked(False)
        # 设置标签
        self.worseFit_action = QtWidgets.QLabel("     Worst fit  ")
        # 设置字体
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        # 设置字体
        self.worseFit_action.setFont(font)
        # 设置style
        self.worseFit_action.setStyleSheet(
            "QLabel { color: rgb(225,225,225);  /*字体颜色*/ \
                background-color:rgb(124,179,66);\
                }"
            "QLabel:hover{ background-color:rgb(51,105,30);/*选中的样式*/ \
                            }"
        )
        # 建立页面
        self.worseFit_bar.setDefaultWidget(self.worseFit_action)


        # 循环首次适应算法按钮
        self.first_crrence_Fit_bar = QtWidgets.QWidgetAction(MainWindow, checkable=True)
        # 设置被选中为False
        self.first_crrence_Fit_bar.setChecked(False)
        # 设置标签
        self.first_crrence_Fit_action = QtWidgets.QLabel("     first_Circuit fit  ")
        # 设置字体
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        # 设置字体
        self.first_crrence_Fit_action.setFont(font)
        # 设置style
        self.first_crrence_Fit_action.setStyleSheet(
            "QLabel { color: rgb(225,225,225);  /*字体颜色*/ \
                background-color:rgb(124,179,66);\
                }"
            "QLabel:hover{ background-color:rgb(51,105,30);/*选中的样式*/ \
                            }"
        )
        # 建立页面
        self.first_crrence_Fit_bar.setDefaultWidget(self.first_crrence_Fit_action)



        #将两按钮添加到model_bar中去
        self.model_bar.addAction(self.firstFit_bar)
        self.model_bar.addAction(self.bestFit_bar)
        self.model_bar.addAction(self.worseFit_bar)
        self.model_bar.addAction(self.first_crrence_Fit_bar)


        # 加入作业lable
        self.lable1 = QtWidgets.QLabel(MainWindow)
        self.lable1.setText("文件：选择分配大小")
        self.lable1.setGeometry(QtCore.QRect(35, 70, 200, 40))


        self.lable2 = QtWidgets.QLabel(MainWindow)
        self.lable2.setText("线程：输入分配大小")
        self.lable2.setGeometry(QtCore.QRect(35, 235, 200, 40))


        self.lable3 = QtWidgets.QLabel(MainWindow)
        self.lable3.setText("访问数据块(输入块号)")
        self.lable3.setGeometry(QtCore.QRect(35, 280, 200, 40))


        # # 创建快捷加入按钮
        self.btnGroup = {}
        # 遍历
        for i in range(0, 8):
            # 创建一个按钮，并将按钮加入到窗口MainWindow中
            self.btnGroup[i] = QtWidgets.QPushButton(MainWindow)
            # 设置字体
            self.btnGroup[i].setFont(QtGui.QFont('Microsoft YaHei', 6))
            # 设置text
            self.btnGroup[i].setText(str((i+1))+'块')
            # 定位
            self.btnGroup[i].setGeometry(QtCore.QRect(((i//4)+1)*35, 100 + (i % 4) * 31, 30, 30))
            # 设置style
            self.btnGroup[i].setStyleSheet("QPushButton{color:rgb(255,255,255)}"
                                           "QPushButton{background-color:rgb(124,179,66)}"
                                           "QPushButton{border: 2px solid rgb(100,100,100)}"
                                           "QPushButton:hover{background-color:rgb(104,159,56)}"
                                           "QPushButton:pressed{background-color:rgb(51,105,30)}")




        # 创建一个文本框，并将按钮加入到窗口MainWindow中
        self.textbox1 = QtWidgets.QLineEdit(MainWindow)
        self.textbox1.setFont(QtGui.QFont('Microsoft YaHei', 10))
        self.textbox1.setGeometry(35, 265, 100, 25)
        self.textbox1.setStyleSheet(
            "QLineEdit{color:rgb(0,0,0)}"  # 按键前景色
            "QLineEdit{background-color:rgb(242,242,242)}"  # 按键背景色
            "QLineEdit:hover{background-color:rgb(255,255,255)}"  # 光标移动到上面后的前景色
            "QLineEdit{border: 2px solid rgb(0,0,0);}"  # 边框
        )

        # 创建一个文本框，并将按钮加入到窗口MainWindow中
        self.textbox2 = QtWidgets.QLineEdit(MainWindow)
        self.textbox2.setFont(QtGui.QFont('Microsoft YaHei', 10))
        self.textbox2.setGeometry(35, 310, 100, 25)
        self.textbox2.setStyleSheet(
            "QLineEdit{color:rgb(0,0,0)}"  # 按键前景色
            "QLineEdit{background-color:rgb(242,242,242)}"  # 按键背景色
            "QLineEdit:hover{background-color:rgb(255,255,255)}"  # 光标移动到上面后的前景色
            "QLineEdit{border: 2px solid rgb(0,0,0);}"  # 边框
        )

        # 限制小数范围
        validator = QDoubleValidator(0, 16, 3)
        self.textbox1.setValidator(validator)
        self.textbox2.setValidator(validator)

        # 创建文本框输入确认按钮，并将按钮加入到窗口MainWindow中
        self.text_btn1 = QtWidgets.QPushButton('OK', MainWindow)
        self.text_btn1.setFont(QtGui.QFont('Microsoft YaHei', 10))
        self.text_btn1.setGeometry(150, 265, 50, 25)
        self.text_btn1.setStyleSheet(
            "QPushButton{color:rgb(255,255,255)}"
            "QPushButton{background-color:rgb(124,179,66)}"
            "QPushButton{border: 2px solid rgb(100,100,100)}"
            "QPushButton:hover{background-color:rgb(150,150,150)}"
            "QPushButton:pressed{background-color:rgb(130,130,130)}")


        # 创建文本框输入确认按钮，并将按钮加入到窗口MainWindow中
        self.text_btn2 = QtWidgets.QPushButton('OK', MainWindow)
        self.text_btn2.setFont(QtGui.QFont('Microsoft YaHei', 10))
        self.text_btn2.setGeometry(150, 310, 50, 25)
        self.text_btn2.setStyleSheet(
            "QPushButton{color:rgb(255,255,255)}"
            "QPushButton{background-color:rgb(124,179,66)}"
            "QPushButton{border: 2px solid rgb(100,100,100)}"
            "QPushButton:hover{background-color:rgb(150,150,150)}"
            "QPushButton:pressed{background-color:rgb(130,130,130)}")


        # 创建重置按钮
        self.clear_btn = QtWidgets.QPushButton('清空内存', MainWindow)
        self.clear_btn.setFont(QtGui.QFont('Microsoft YaHei', 9))
        self.clear_btn.setGeometry(445, 265, 60, 25)
        self.clear_btn.setStyleSheet(
            "QPushButton{color:rgb(80,80,80)}"
            "QPushButton{background-color:rgb(190,190,190)}"
            "QPushButton{border: 2px solid rgb(130,130,130)}"
            "QPushButton:hover{background-color:rgb(150,150,150)}"
            "QPushButton:pressed{background-color:rgb(130,130,130)}")

    # 刷新页面
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("内存管理", "Voice Assistant"))


# 我的窗口
class myWindow(QtWidgets.QMainWindow):


    # 初始化
    def __init__(self):
        super(myWindow, self).__init__()
        self.myCommand = " "
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # firstFit模式触发
        self.ui.firstFit_bar.triggered.connect(self.firstFitbar_recognize)
        # bestFit模式触发
        self.ui.bestFit_bar.triggered.connect(self.bestFitbar_recognize)
        # worseFit模式触发
        self.ui.worseFit_bar.triggered.connect(self.worseFitbar_recognize)
        # first_currenceFit模式触发
        self.ui.first_crrence_Fit_bar.triggered.connect(self.first_currence_Fit_bar_recognize)


        # 文本框输入确认按钮连接文本处理函数
        self.ui.text_btn1.clicked.connect(self.text_changed1)
        # 文本框输入响应enter键
        self.ui.textbox1.returnPressed.connect(self.text_changed1)


        # 文本框输入确认按钮连接文本处理函数
        self.ui.text_btn2.clicked.connect(self.text_changed2)
        # 文本框输入响应enter键
        self.ui.textbox2.returnPressed.connect(self.text_changed2)


        # Reset按钮连接重置内存空间函数
        self.ui.clear_btn.clicked.connect(self.clear)


        for i in range(0, 8):
            self.ui.btnGroup[i].clicked.connect(
                partial(self.addNode, (i+1), 'F'))
        self.isbestFit = False
        self.isfirst = True
        self.isworse = False
        self.isfirst_currence = False
        self.workNumber = 1  # 作业个数
        self.nodeList = []  # 结点链表
        # 初始化，将40k视为一个空结点
        self.nodeList.insert(0, {'number': -1,  # 非作业结点
                                 'start': 4+data,  # 开始为4+data
                                 'length': 12-data,  # 长度为12-data
                                 'isnull': True,
                                 'time':time.time(),
                                 'classes':'F'})  # 空闲
        # 初始化，加入操作系统4
        self.nodeList.insert(1, {'number': 1,  # 非作业结点
                                 'start': 0,  # 开始为0
                                 'length': 4,  # 长度为4
                                 'isnull': False,
                                 'time':time.time(),
                                 'classes':'P'})  # 空闲

        # 初始化，加入操作系统24k
        self.nodeList.insert(2, {'number': 2,  # 非作业结点
                                 'start': 4,  # 开始为0
                                 'length': data,  # 长度为4
                                 'isnull': False,
                                 'time':time.time(),
                                 'classes':'P'})  # 空闲

        print(self.nodeList)
        # 加入一个非作业btn
        self.nodeList[0]['btn'] = self.addButton(self.nodeList[0],'P')

        # 添加操作系统
        self.nodeList[1]['btn'] = self.addButton(self.nodeList[1], 'OS')

        self.nodeList[1]['btn'].clicked.connect(
            partial(self.deleteNode, 'OS'))


        self.nodeList[2]['btn'] = self.addButton(self.nodeList[2], 'P')
        self.nodeList[2]['btn'].clicked.connect(
            partial(self.deleteNode, self.nodeList[2]['number']))


    # firstFit从未选状态转变为已选状态时会触发firstFitbar_recognize函数
    def firstFitbar_recognize(self):
        self.ui.firstFit_bar.setChecked(True)
        self.ui.bestFit_bar.setChecked(False)
        self.ui.worseFit_bar.setChecked(False)
        self.ui.first_crrence_Fit_bar.setChecked(False)

        self.ui.firstFit_action.setText(" √  First fit  ")
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.ui.firstFit_action.setFont(font)
        self.ui.firstFit_action.setStyleSheet(
            "QLabel { color: rgb(255,255,255);  /*字体颜色*/ \
                background-color:rgb(51,105,30);\
                }"
            "QLabel:hover{  background-color:rgb(51,105,30);/*选中的样式*/ \
                }"
        )
        self.isfirst = True

        self.ui.bestFit_action.setText("     Best fit  ")
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.ui.bestFit_action.setFont(font)
        self.ui.bestFit_action.setStyleSheet(
            "QLabel { color: rgb(225,225,225);  /*字体颜色*/ \
                background-color:rgb(124,179,66);\
                }"
            "QLabel:hover{ background-color:rgb(51,105,30);/*选中的样式*/ \
                            }"
        )
        self.isbestFit = False

        self.ui.worseFit_action.setText("     Worst fit  ")
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.ui.worseFit_action.setFont(font)
        self.ui.worseFit_action.setStyleSheet(
            "QLabel { color: rgb(225,225,225);  /*字体颜色*/ \
                background-color:rgb(124,179,66);\
                }"
            "QLabel:hover{ background-color:rgb(51,105,30);/*选中的样式*/ \
                            }"
        )
        self.isworse = False

        self.ui.first_crrence_Fit_action.setText("     first_Circuit fit  ")
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.ui.first_crrence_Fit_action.setFont(font)
        self.ui.first_crrence_Fit_action.setStyleSheet(
            "QLabel { color: rgb(225,225,225);  /*字体颜色*/ \
                background-color:rgb(124,179,66);\
                }"
            "QLabel:hover{ background-color:rgb(51,105,30);/*选中的样式*/ \
                            }"
        )
        self.isfirst_currence = False


    # bestFit从未选状态转变为已选状态时会触发bestFitbar_recognize函数
    def bestFitbar_recognize(self):
        self.ui.bestFit_bar.setChecked(True)
        self.ui.firstFit_bar.setChecked(False)
        self.ui.worseFit_bar.setChecked(False)
        self.ui.first_crrence_Fit_bar.setChecked(False)

        self.ui.firstFit_action.setText("     First fit  ")
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.ui.firstFit_action.setFont(font)
        self.ui.firstFit_action.setStyleSheet(
            "QLabel { color: rgb(225,225,225);  /*字体颜色*/ \
                background-color:rgb(124,179,66);\
                }"
            "QLabel:hover{ background-color:rgb(51,105,30);/*选中的样式*/ \
                            }"
        )
        self.isfirst = False

        self.ui.bestFit_action.setText(" √  Best fit  ")
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.ui.bestFit_action.setFont(font)
        self.ui.bestFit_action.setStyleSheet(
            "QLabel { color: rgb(255,255,255);  /*字体颜色*/ \
                background-color:rgb(51,105,30);\
                }"
            "QLabel:hover{  background-color:rgb(51,105,30);/*选中的样式*/ \
                }"
        )
        self.isbestFit = True

        self.ui.worseFit_action.setText("     Worst fit  ")
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.ui.worseFit_action.setFont(font)
        self.ui.worseFit_action.setStyleSheet(
            "QLabel { color: rgb(225,225,225);  /*字体颜色*/ \
                background-color:rgb(124,179,66);\
                }"
            "QLabel:hover{ background-color:rgb(51,105,30);/*选中的样式*/ \
                            }"
        )
        self.isworse = False

        self.ui.first_crrence_Fit_action.setText("     first_Circuit fit  ")
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.ui.first_crrence_Fit_action.setFont(font)
        self.ui.first_crrence_Fit_action.setStyleSheet(
            "QLabel { color: rgb(225,225,225);  /*字体颜色*/ \
                background-color:rgb(124,179,66);\
                }"
            "QLabel:hover{ background-color:rgb(51,105,30);/*选中的样式*/ \
                            }"
        )
        self.isfirst_currence = False


    # worseFit从未选状态转变为已选状态时会触发worseFitbar_recognize函数
    def worseFitbar_recognize(self):
        self.ui.worseFit_bar.setChecked(True)
        self.ui.firstFit_bar.setChecked(False)
        self.ui.bestFit_bar.setChecked(False)
        self.ui.first_crrence_Fit_bar.setChecked(False)

        self.ui.firstFit_action.setText("     first fit  ")
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.ui.firstFit_action.setFont(font)
        self.ui.firstFit_action.setStyleSheet(
            "QLabel { color: rgb(225,225,225);  /*字体颜色*/ \
                background-color:rgb(124,179,66);\
                }"
            "QLabel:hover{ background-color:rgb(51,105,30);/*选中的样式*/ \
                            }"
        )
        self.isfirst = False

        self.ui.worseFit_action.setText(" √  Worse fit  ")
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.ui.worseFit_action.setFont(font)
        self.ui.worseFit_action.setStyleSheet(
            "QLabel { color: rgb(255,255,255);  /*字体颜色*/ \
                background-color:rgb(51,105,30);\
                }"
            "QLabel:hover{  background-color:rgb(51,105,30);/*选中的样式*/ \
                }"
        )
        self.isworse = True

        self.ui.bestFit_action.setText("     Best fit  ")
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.ui.bestFit_action.setFont(font)
        self.ui.bestFit_action.setStyleSheet(
            "QLabel { color: rgb(225,225,225);  /*字体颜色*/ \
                background-color:rgb(124,179,66);\
                }"
            "QLabel:hover{ background-color:rgb(51,105,30);/*选中的样式*/ \
                            }"
        )
        self.isbestFit = False


        self.ui.first_crrence_Fit_action.setText("     first_Circuit fit  ")
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.ui.first_crrence_Fit_action.setFont(font)
        self.ui.first_crrence_Fit_action.setStyleSheet(
            "QLabel { color: rgb(225,225,225);  /*字体颜色*/ \
                background-color:rgb(124,179,66);\
                }"
            "QLabel:hover{ background-color:rgb(51,105,30);/*选中的样式*/ \
                            }"
        )
        self.isfirst_currence = False


    # first_crruce_Fit从未选状态转变为已选状态时会触发crruce_Fitbar_recognize函数
    def first_currence_Fit_bar_recognize(self):
        self.ui.worseFit_bar.setChecked(False)
        self.ui.firstFit_bar.setChecked(False)
        self.ui.bestFit_bar.setChecked(False)
        self.ui.first_crrence_Fit_bar.setChecked(True)


        self.ui.first_crrence_Fit_action.setText(" √  first_Circuit fit  ")
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.ui.first_crrence_Fit_action.setFont(font)
        self.ui.first_crrence_Fit_action.setStyleSheet(
            "QLabel { color: rgb(255,255,255);  /*字体颜色*/ \
                background-color:rgb(51,105,30);\
                }"
            "QLabel:hover{  background-color:rgb(51,105,30);/*选中的样式*/ \
                }"
        )
        self.isfirst_currence = True


        self.ui.firstFit_action.setText("    first fit  ")
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.ui.firstFit_action.setFont(font)
        self.ui.firstFit_action.setStyleSheet(
            "QLabel { color: rgb(225,225,225);  /*字体颜色*/ \
                background-color:rgb(124,179,66);\
                }"
            "QLabel:hover{ background-color:rgb(51,105,30);/*选中的样式*/ \
                            }"
        )
        self.isfirst = False

        self.ui.worseFit_action.setText("    Worse fit  ")
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.ui.worseFit_action.setFont(font)
        self.ui.worseFit_action.setStyleSheet(
            "QLabel { color: rgb(225,225,225);  /*字体颜色*/ \
                background-color:rgb(124,179,66);\
                }"
            "QLabel:hover{ background-color:rgb(51,105,30);/*选中的样式*/ \
                            }"
        )
        self.isworse = False


        self.ui.bestFit_action.setText("     Best fit  ")
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.ui.bestFit_action.setFont(font)
        self.ui.bestFit_action.setStyleSheet(
            "QLabel { color: rgb(225,225,225);  /*字体颜色*/ \
                background-color:rgb(124,179,66);\
                }"
            "QLabel:hover{ background-color:rgb(51,105,30);/*选中的样式*/ \
                            }"
        )
        self.isbestFit = False


    # 重置内存空间函数
    def clear(self):
        # 弹出提示框
        reply = QMessageBox.information(self,
                                        "消息",
                                        "确定清空内存？",
                                        QMessageBox.Yes | QMessageBox.No)
        # 是否进入内存查看
        if reply == 65536:
            return
        else:
            pass

        now = 0
        self.workNumber = 1  # 作业个数
        self.nodeList = []  # 结点链表
        # 初始化，将40视为一个空结点
        self.nodeList.insert(0, {'number': -1,  # 非作业结点
                                 'start': 4,  # 开始为0
                                 'length': 12,  # 长度为12
                                 'isnull': True,
                                 'time':time.time(),
                                 'classes':'F'})  # 空闲
        # 初始化，加入操作系统4
        self.nodeList.insert(1, {'number': 1,  # 非作业结点
                                 'start': 0,  # 开始为0
                                 'length': 4,  # 长度为4
                                 'isnull': False,
                                 'time':time.time(),
                                 'classes':'P'})  # 空闲
        # 加入一个非作业btn
        self.nodeList[0]['btn'] = self.addButton(self.nodeList[0], 'P')

        # 添加操作系统
        self.nodeList[1]['btn'] = self.addButton(self.nodeList[1], 'OS')

        self.nodeList[1]['btn'].clicked.connect(
            partial(self.deleteNode, 'OS'))
        size = len(self.nodeList)
        for i in range(1, size):
            self.nodeList.pop()


    # 寻找首次适应算法添加结点的位置
    def findFirstNode(self, length):
        self.targetNumber = -1
        for i in range(0, len(self.nodeList)):
            # 如果结点i为空闲
            if self.nodeList[i]['isnull'] and self.nodeList[i]['length'] >= length:
                self.targetNumber = i
                return self.targetNumber
        return -1


    # 寻找循环首次适应算法添加结点的位置
    def findFirst_currence_Node(self, length,now):
        self.targetNumber = -1
        for i in range(now, len(self.nodeList)):
            # 如果结点i为空闲
            if self.nodeList[i]['isnull'] and self.nodeList[i]['length'] >= length:
                self.targetNumber = i
                now = self.targetNumber
                return self.targetNumber
        now = 0
        return -1


    # 寻找最佳适应算法添加结点的位置
    def findBestNode(self, length):
        self.min = 17
        self.targetNumber = -1
        for i in range(0, len(self.nodeList)):
            # 如果结点i为空闲
            if self.nodeList[i]['isnull'] and (self.min > self.nodeList[i]['length'] >= length):
                self.min = self.nodeList[i]['length']
                self.targetNumber = i
        return self.targetNumber


    # 最差适应算法添加结点的位置
    def findWorseNode(self,length):
        self.max = 0
        self.targetNumber = -1
        for i in range(0, len(self.nodeList)):
            # 如果结点i为空闲
            if self.nodeList[i]['isnull'] and (self.max < self.nodeList[i]['length'] >= length):
                self.max = self.nodeList[i]['length']
                self.targetNumber = i
        return self.targetNumber


    # 添加结点
    def addNode(self, length, classes):
        if self.isbestFit:
            i = self.findBestNode(length)
        if self.isfirst:
            i = self.findFirstNode(length)
        if self.isworse:
            i = self.findWorseNode(length)
        if self.isfirst_currence:
            i = self.findFirst_currence_Node(length,now)
        if i==-1:
            # 弹出提示框
            reply = QMessageBox.information(self,
                                            "消息",
                                            "内存不足,是否置换？",
                                            QMessageBox.Yes|QMessageBox.No)
            if reply == 65536:
                pass
            else:
                min = self.nodeList[0]['time']
                min_index = self.nodeList[0]['number']
                for j in range(0,len(self.nodeList)):
                    if min > self.nodeList[j]['time'] and self.nodeList[j]['isnull']== False and self.nodeList[j]['number']!=1:
                        min = self.nodeList[j]['time']
                        min_index = self.nodeList[j]['number']
                print(min_index,time.ctime(min))
                self.deleteNode(min_index)

        if self.isbestFit:
            i = self.findBestNode(length)
        if self.isfirst:
            i = self.findFirstNode(length)
        if self.isworse:
            i = self.findWorseNode(length)
        if self.isfirst_currence:
            i = self.findFirst_currence_Node(length,now)


        if i >= 0:
            self.workNumber += 1  # 作业数量+1
            if self.nodeList[i]['length'] > length:
                # 在该结点后插入新的作业结点
                self.nodeList.insert(i+1, {'number': self.workNumber,  # 作业workNumber
                                           'start': self.nodeList[i]['start'],  # 开始为结点i的开始
                                           'length': length,  # 长度
                                           'isnull': False,
                                           'time':time.time(),
                                           'classes':classes})  # 不空闲
                # 加入一个作业btn
                self.nodeList[i+1]['btn'] = self.addButton(self.nodeList[i+1], classes)
                self.nodeList[i+1]['btn'].clicked.connect(
                    partial(self.deleteNode, self.nodeList[i+1]['number']))
                # 将剩下的部分置为空白结点
                self.nodeList.insert(i+2, {'number': -1,  # 非作业结点
                                           'start': self.nodeList[i+1]['start']+length,  # 开始为i+1的开始+length
                                           'length': self.nodeList[i]['length']-length,  # 长度为结点i的长度-length
                                           'isnull': True,
                                           'time':time.time(),
                                           'classes':classes})  # 空闲
                # 加入一个非作业btn
                self.nodeList[i+2]['btn'] = self.addButton(self.nodeList[i+2], classes)
                # 删除结点i
                del self.nodeList[i]
            # 空闲结点i的长度等于所需长度
            elif self.nodeList[i]['length'] == length:
                # 在该结点后插入新的作业结点
                self.nodeList.insert(i + 1, {'number': self.workNumber,  # 作业workNumber
                                             'start': self.nodeList[i]['start'],  # 开始为结点i的开始
                                             'length': length,  # 长度
                                             'isnull': False,
                                            'time':time.time(),
                                             'classes':classes})  # 不空闲
                # 插入一个作业btn
                self.nodeList[i + 1]['btn'] = self.addButton(self.nodeList[i+1])
                self.nodeList[i + 1]['btn'].clicked.connect(
                    partial(self.deleteNode, self.nodeList[i + 1]['number']))
                # 删除结点i
                del self.nodeList[i]


    # 删除作业结点
    def deleteNode(self, workNumber):
        if workNumber=='OS':
            reply = QMessageBox.warning(self,
                                            "消息",
                                            "没有权限",
                                            QMessageBox.Ok)

        self.current = -1
        # 寻找目标删除结点
        for i in range(0, len(self.nodeList)):
            if self.nodeList[i]['number'] == workNumber:
                self.current = i
                break
        # 找到目标删除结点
        if self.current != -1:
            # 前后都无空闲结点
            if (self.current == 0 or bool(1-self.nodeList[self.current - 1]['isnull'])) \
                    and (self.current == len(self.nodeList) - 1 or bool(1-self.nodeList[self.current + 1]['isnull'])):
                self.nodeList.insert(self.current + 1, {'number': -1,  # 非作业结点
                                                        # 开始为self.current结点的开始
                                                        'start': self.nodeList[self.current]['start'],
                                                        # 长度为结点self.current长度
                                                        'length': self.nodeList[self.current]['length'],
                                                        'isnull': True,
                                                        'time':time.time()
                                                        })  # 空闲
                # 加入一个非作业btn
                self.nodeList[self.current + 1]['btn'] = self.addButton(self.nodeList[self.current+1],'P')
                del self.nodeList[self.current]
            else:
                # 结点非头结点且其前一个结点是空闲结点
                if self.current-1 >= 0 and self.nodeList[self.current-1]['isnull']:
                    # 将两部分合为一个空白结点
                    self.nodeList.insert(self.current + 1, {'number': -1,  # 非作业结点
                                                             # 开始为self.current-1结点的开始
                                                             'start': self.nodeList[self.current - 1]['start'],
                                                             # 长度为结点self.current-1的长度+结点self.current的长度
                                                             'length': self.nodeList[self.current-1]['length']
                                                                       + self.nodeList[self.current]['length'],
                                                             'isnull': True,
                                                            'time':time.time()})  # 空闲
                    # 加入一个非作业btn
                    self.nodeList[self.current + 1]['btn'] = self.addButton(self.nodeList[self.current+1], 'P')
                    # 删除原来两结点
                    del self.nodeList[self.current-1]
                    # 删除current
                    del self.nodeList[self.current-1]
                    self.current -= 1
                # 结点非尾结点且其后一个结点为空白结点
                if self.current < len(self.nodeList)-1 and self.nodeList[self.current+1]['isnull']:
                    # 将两部分合为一个空白结点
                    self.nodeList.insert(self.current + 2, {'number': -1,  # 非作业结点
                                                            # 开始为self.current结点的开始
                                                           'start': self.nodeList[self.current]['start'],
                                                           # 长度为结点self.current的长度+结点self.current+1的长度
                                                           'length': self.nodeList[self.current]['length']
                                                                     + self.nodeList[self.current + 1]['length'],
                                                           'isnull': True,
                                                            'time':time.time()})  # 空闲
                    # 加入一个非作业btn
                    self.nodeList[self.current + 2]['btn'] = self.addButton(self.nodeList[self.current+2],'P')
                    # 删除原来两结点
                    del self.nodeList[self.current]
                    # 删除current+1
                    del self.nodeList[self.current]


    # 加入作业
    def addButton(self, node=[], classes = 'P'):
        # 空闲结点按钮
        if node['isnull']:
            btn = QtWidgets.QPushButton(str(node['length'])+'块', self)
            btn.setFont(QtGui.QFont('Microsoft YaHei', node['length']/42*15 + 5))
            btn.setGeometry(280, 30 + node['start']*15, 150, node['length']*15)
            # 设置style
            btn.setStyleSheet(
                "QPushButton{color:rgb(150,150,150)}"
                "QPushButton{background-color:rgb(240,240,240)}"
                "QPushButton{border: 1.5px solid rgb(66,66,66);}"
            )
            btn.setVisible(True)
        # 作业结点按钮
        else:
            if node['number']==1:
                btn = QtWidgets.QPushButton('OS' + ':\n' + str(node['length']) + '块', self)
            else:
                btn = QtWidgets.QPushButton(classes+str(node['number'])+':\n'+str(node['length'])+'块', self)
            # 设置字体
            btn.setFont(QtGui.QFont('Microsoft YaHei', node['length'] / 42 * 4 + 5))
            # 设置位置
            btn.setGeometry(280, 30 + node['start']*15, 150, node['length']*15)
            # 设置style
            btn.setStyleSheet(
                "QPushButton{color:rgb(1,0,0)}"
                "QPushButton{background-color:rgb(124,179,66)}"
                "QPushButton:hover{background-color:rgb(210,210,210)}"
                "QPushButton:pressed{background-color:rgb(200,200,200)}"
                "QPushButton{border: 1.5px solid rgb(66,66,66);}"
            )
            btn.setVisible(True)
        return btn


    #文本处理函数
    def text_changed1(self):
        if self.ui.textbox1.text() == '':
            self.content = 0
        else:
            self.content = 0
            if ('.' not in self.ui.textbox1.text()):
                self.content = int(self.ui.textbox1.text())
            else:
                self.content = float(self.ui.textbox1.text())
        self.ui.textbox1.setText('')
        if self.content <= 12:
            self.addNode(self.content,'P')
        else:
            reply = QMessageBox.information(self,
                                            "消息",
                                            "超过最大内存，无法分配！",
                                            QMessageBox.Ok)

    #文本处理函数
    def text_changed2(self):
        for i in self.nodeList:
            if i['number'] == int(self.ui.textbox2.text()):
                print(time.ctime(i['time']))
                reply = QMessageBox.information(self,
                                                "消息",
                                                "访问成功:"+'\n'+
                                                "      数据块名："+
                                                str(i["number"])+
                                                "\n" +'            类型：'+
                                                i['classes'] +
                                                '\n'+
                                                "进入内存时间："+str(time.ctime(i['time']))+'\n'+
                                                "      访问时间："+str(time.ctime()),
                                                QMessageBox.Ok)
                return
                print(i['time'])


        reply = QMessageBox.information(self,
                                        "消息",
                                        "访问失败，该进程不在内存中",
                                        QMessageBox.Ok)


# 主函数
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    try:
        data = int(app.arguments()[1])
    except:
        pass
    application = myWindow()
    application.show()
    sys.exit(app.exec_())


