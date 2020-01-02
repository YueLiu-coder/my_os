# 导入所需要的python包
import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QPushButton, QLabel, QMessageBox
from PyQt5.QtCore import QObject, Qt, pyqtSignal
from PyQt5.QtGui import QPainter, QColor, QPen
import numpy as np
import os
from thread import *
import _thread


# Communicate类
class Communicate(QObject):
    # 更新页面
    update_widget = pyqtSignal(int, int)


# 磁盘对换区占用条类，继承QWidget类，所有用户界面对象的基类
class DrawWidget_cache(QWidget):
    # 记录已经被使用的的列表
    used_val_list = []
    used_add_val_list = []
    used_dict = {}
    used_index = 0

    # 定义颜色块列表
    color_list = []

    # 开始值
    start_add = 0
    # 结束值
    end_add = 0

    # 初始标志
    init_flag = True

    # 初始化函数
    def __init__(self, parent=None):
        # 继承Qwidget的初始化函数
        super(QWidget, self).__init__(parent)
        # 初始化UI界面
        self.initUI()

    # 初始化UI界面函数
    def initUI(self):
        # 定位鼠标
        self.setMouseTracking(True)
        # 设置占用条的大小
        self.setMinimumSize(1, 30)

    # 设置值
    def setValue(self, start_val, end_val):
        # 设置开始值
        self.start_add = start_val
        # 设置结束值
        self.end_add = end_val

        # 装入被使用列表中
        self.used_val_list.append(self.start_add)
        # 装入被使用列表中
        self.used_val_list.append(self.end_add)
        # 使用的index+1
        self.used_index += 1

    # 画图事件
    def paintEvent(self, e):
        # 调用Qpainter
        qp = QPainter()
        # 开始画图
        qp.begin(self)
        # 调用画对换区占用条函数
        self.drawWidget(qp)
        # 画图结束
        qp.end()

    # 画对换区占用条函数
    def drawWidget(self, qp):
        # 外框线，设置为黑色
        pen = QPen(QColor(0, 0, 0), 0.1, Qt.SolidLine)
        # 设置pen
        qp.setPen(pen)
        # 设置setBrush为白色，代表空磁盘区
        qp.setBrush(QColor(255, 255, 255))
        # 画出图，按照x,y,宽和高
        qp.drawRect(0, 0, self.size().width() - 1, self.size().height() - 1)

        # 开始值
        start_val = int(((self.size().width() / 124) * self.start_add))
        # 结束值
        end_val = int(((self.size().width() / 124) * self.end_add))

        # 使用掉的列表
        self.used_add_val_list = [self.start_add, self.end_add, start_val, end_val]
        # 使用掉的字典
        self.used_dict[self.used_index] = self.used_add_val_list

        # 画出对换区占用条使用情况
        for i in range(self.used_index + 1):
            qp.setPen(pen)
            try:
                qp.setBrush(QColor(self.color_list[i][0], self.color_list[i][1], self.color_list[i][2]))
            except:
                r = np.random.randint(0, 255)
                g = np.random.randint(0, 255)
                b = np.random.randint(0, 255)
                qp.setBrush(QColor(r, g, b))
                self.color_list.append([r, g, b])

            qp.drawRect(self.used_dict.get(i)[3], 0, self.used_dict.get(i)[2] - self.used_dict.get(i)[3],
                        self.size().height() - 1)

    # 寻找序列
    def sequencesearch(self, value):
        #
        value = (value * 124) / self.size().width()
        # 将使用的列表排序
        self.used_val_list.sort()
        # 遍历使用的列表
        for i in range(len(self.used_val_list)):
            # 如果在中间段
            if value > self.used_val_list[i] and value < self.used_val_list[i + 1]:
                # 返回中间值
                return self.used_val_list[i], self.used_val_list[i + 1]
            # 如果在最后
            elif value > self.used_val_list[-1]:
                # 返回最后一个元素,124
                return self.used_val_list[-1], 124
            # 如果在最前,且分配了空间
            elif value < self.used_val_list[0] and self.used_val_list[0] != 0:
                # 返回0,第一个元素
                return 0, self.used_val_list[0]
        # 否则返回-1
        return -1

    # 鼠标移动事件
    def mouseMoveEvent(self, a0: QtGui.QMouseEvent):
        # 如果鼠标移动的x输入到sequencesearch后得到-1(没有找到) 或者 不存在
        if self.sequencesearch(a0.x()) == -1 or self.sequencesearch(a0.x()) == None:
            # 设置tip为空
            self.setToolTip('空对换区')
            # 返回
            return
        # 否则
        else:
            # 获取到开始值和结束值
            start_val, end_val = self.sequencesearch(a0.x())
            # 设置tip
            self.setToolTip(
                # 开始到结束,设置为16进制
                str(hex(start_val)[2:].zfill(2).upper()) + '-' + str(hex(end_val)[2:].zfill(2).upper()))


# 磁盘文件区占用条类，继承QWidget类，所有用户界面对象的基类
class DrawWidget_file(QWidget):
    # 开始值
    start_add = 0
    # 结束值
    end_add = 300
    # 定义颜色列表
    color_list = []
    # 记录已经被使用的的列表
    used_val_list = [0, 300]
    used_add_val_list = []
    used_dict = {}
    used_index = 0

    # used_index += 1

    # 初始化函数
    def __init__(self, parent=None):
        # 继承Qwidget的初始化函数
        super(QWidget, self).__init__(parent)
        # 初始化UI界面
        self.initUI()
        self.color_list = []

    # 初始化UI界面函数
    def initUI(self):
        # 定位鼠标
        self.setMouseTracking(True)
        # 设置占用条的大小
        self.setMinimumSize(1, 30)

    # 设置值
    def setValue(self, start_val, end_val):
        # 设置开始值
        self.start_add = start_val
        # 设置结束值
        self.end_add = end_val

        # 装入被使用列表中
        self.used_val_list.append(self.start_add)
        # 装入被使用列表中
        self.used_val_list.append(self.end_add)
        # 使用的index+1
        self.used_index += 1

    # 画图事件
    def paintEvent(self, e):
        # 调用Qpainter
        qp_file = QPainter()
        # 开始画图
        qp_file.begin(self)
        # 调用画文件区占用条函数
        self.drawWidget(qp_file)
        # 画图结束
        qp_file.end()

    # 画文件区占用条函数
    def drawWidget(self, qp_file):
        # 外框线，设置为黑色
        pen = QPen(QColor(0, 0, 0), 0.1, Qt.SolidLine)
        # 设置pen
        qp_file.setPen(pen)
        # 设置setBrush为白色，代表空磁盘区
        qp_file.setBrush(QColor(255, 255, 255))
        # 画出图，按照x,y,宽和高
        qp_file.drawRect(0, 0, self.size().width() - 1, self.size().height() - 1)

        # 开始值
        start_val = int(((self.size().width() / 900) * self.start_add))
        # print(self.start_add)
        # print(start_val)
        # 结束值
        end_val = int(((self.size().width() / 900) * self.end_add))
        # print(end_val)

        # 使用掉的列表
        self.used_add_val_list = [self.start_add, self.end_add, start_val, end_val]
        # 使用掉的字典
        self.used_dict[self.used_index] = self.used_add_val_list

        # 画出对换区占用条使用情况
        for i in range(self.used_index + 1):
            qp_file.setPen(pen)
            try:
                qp_file.setBrush(QColor(self.color_list[i][0], self.color_list[i][1], self.color_list[i][2]))
            except:
                r = np.random.randint(0, 255)
                g = np.random.randint(0, 255)
                b = np.random.randint(0, 255)
                qp_file.setBrush(QColor(r, g, b))
                self.color_list.append([r, g, b])

            qp_file.drawRect(self.used_dict.get(i)[3], 0, self.used_dict.get(i)[2] - self.used_dict.get(i)[3],
                             self.size().height() - 1)

    # 寻找序列函数
    def sequencesearch(self, value):
        value = (value * 900) / self.size().width()
        self.used_val_list.sort()
        for i in range(len(self.used_val_list)):
            if value > self.used_val_list[i] and value < self.used_val_list[i + 1]:
                return self.used_val_list[i], self.used_val_list[i + 1]
            elif value > self.used_val_list[-1]:
                return self.used_val_list[-1], 900
            elif value < self.used_val_list[0] and self.used_val_list[0] != 0:
                return 0, self.used_val_list[0]
        return -1

    # 鼠标移动事件
    def mouseMoveEvent(self, a0: QtGui.QMouseEvent):
        # 如果鼠标移动的x输入到sequencesearch后得到-1(没有找到) 或者 不存在
        if self.sequencesearch(a0.x()) == -1 or self.sequencesearch(a0.x()) == None:
            # 设置tip为空
            self.setToolTip('空文件区')
            # 返回
            return
        # 否则
        else:
            # 获取到开始值和结束值
            start_val, end_val = self.sequencesearch(a0.x())
            # 设置tip
            self.setToolTip(
                # 开始到结束,设置为16进制
                str(hex(start_val)[2:].zfill(4).upper()) + '-' + str(hex(end_val)[2:].zfill(4).upper()))


# Space类，继承QWidget类，所有用户界面对象的基类
class Space(QWidget):
    # 初始化
    def __init__(self, parent=None):
        # 继承Qwidget类的初始化__init__
        super(QWidget, self).__init__(parent)
        # 初始化UI界面
        self.initUI()

    # 初始化UI界面函数
    def initUI(self):
        # 设置输入框text1
        self.text1 = QLineEdit(self)
        # 定位输入框text1的位置
        self.text1.setGeometry(30, 70, 100, 30)

        # 设置输入框text2
        self.text2 = QLineEdit(self)
        # 定位输入框text2的位置
        self.text2.setGeometry(160, 70, 100, 30)

        # 设置按钮btn1
        self.btn1 = QPushButton(self)
        # 设置按钮btn1的名字
        self.btn1.setText("申请调入对换区")
        # 定位按钮btn1的位置
        self.btn1.setGeometry(290, 70, 100, 30)

        # 设置按钮btn2
        self.btn2 = QPushButton(self)
        # 设置按钮btn2的名字
        self.btn2.setText("清空对换区")
        # 定位按钮btn2的位置
        self.btn2.setGeometry(420, 70, 100, 30)

        # 设置按钮btn3
        self.btn3 = QPushButton(self)
        # 设置按钮btn3的名字
        self.btn3.setText("文件区格式化")
        # 定位按钮btn2的位置
        self.btn3.setGeometry(420, 250, 100, 30)

        # 设置按钮btn4
        self.btn4 = QPushButton(self)
        # 设置按钮btn4的名字
        self.btn4.setText("调入文件区保存")
        # 定位按钮btn4的位置
        self.btn4.setGeometry(420, 110, 100, 30)

        # 设置按钮btn5
        self.btn5 = QPushButton(self)
        # 设置按钮btn5的名字
        self.btn5.setText("申请调出对换区")
        # 定位按钮btn5的位置
        self.btn5.setGeometry(290, 110, 100, 30)

        # 定义Communicate类，用于刷新页面
        self.communicate = Communicate(self)

        # 画出对换区的使用条
        self.widget = DrawWidget_cache(self)
        self.widget.setGeometry(30, 140, 500, 10)

        # 画出文件区的使用条
        self.widget2 = DrawWidget_file(self)
        self.widget2.setGeometry(30, 320, 500, 900 / 124 * 10)

        # 设置label
        self.lab1 = QLabel(self)
        self.lab2 = QLabel(self)
        self.lab3 = QLabel(self)
        self.lab4 = QLabel(self)
        self.lab5 = QLabel(self)
        self.lab6 = QLabel(self)
        self.lab7 = QLabel(self)
        self.lab8 = QLabel(self)
        self.lab9 = QLabel(self)
        self.lab10 = QLabel(self)
        self.lab11 = QLabel(self)
        self.lab12 = QLabel(self)

        self.lab1.setText("对换区")
        self.lab1.setGeometry(260, 20, 70, 20)

        self.lab2.setText("起始地址")
        self.lab2.setGeometry(30, 50, 70, 20)

        self.lab3.setText("对换区磁盘使用情况(共124块,1块=4B)")
        self.lab3.setGeometry(30, 120, 230, 20)

        self.lab4.setText("文件区")
        self.lab4.setGeometry(260, 200, 70, 20)

        self.lab5.setText("文件区磁盘使用情况(共900块,1块=4B)")
        self.lab5.setGeometry(30, 300, 230, 20)

        self.lab6.setText("分配块数")
        self.lab6.setGeometry(160, 50, 100, 20)

        # 计算当前块数
        sum = 0
        for i in range(0, len(self.widget.used_val_list), 2):
            sum += self.widget.used_val_list[i + 1] - self.widget.used_val_list[i]
        self.lab7.setText("当前使用块数:" + str(sum))
        self.lab7.setGeometry(30, 170, 230, 20)
        self.lab8.setText("当前剩余块数:" + str(124 - sum))
        self.lab8.setGeometry(200, 170, 230, 20)
        useage = format(float(sum) / float(124) * 100, '.2f')
        self.lab9.setText("当前使用率:" + str(useage) + '%')
        self.lab9.setGeometry(370, 170, 230, 20)

        # 计算当前块数
        sum = 0
        for i in range(0, len(self.widget2.used_val_list), 2):
            sum += self.widget2.used_val_list[i + 1] - self.widget2.used_val_list[i]
        self.lab10.setText("当前使用块数:" + str(sum))
        self.lab10.setGeometry(30, 390, 230, 20)
        self.lab11.setText("当前剩余块数:" + str(900 - sum))
        self.lab11.setGeometry(200, 390, 230, 20)
        useage = format(float(sum) / float(900) * 100, '.2f')
        self.lab12.setText("当前使用率:" + str(useage) + '%')
        self.lab12.setGeometry(370, 390, 230, 20)

        # 连接设置值函数
        self.communicate.update_widget[int, int].connect(self.widget.setValue)
        # 连接改变对换区函数
        self.btn1.clicked.connect(self.changeValue)
        # 连接清空对换区函数
        self.btn2.clicked.connect(self.clearValue)
        # 连接格式化文件区函数
        self.btn3.clicked.connect(self.file_format)
        # 连接调入文件区函数
        self.btn4.clicked.connect(self.to_file)
        # 申请调出对换区函数
        self.btn5.clicked.connect(self.to_ram)


        # 设置总页面的大小和位置
        self.setGeometry(370, 150, 600, 430)
        # 给总页面取名字
        self.setWindowTitle("磁盘管理")
        # 显示
        self.show()

    # 调入对换区按钮
    def changeValue(self):
        try:
            # 将text1的输入转换为int类型
            val1 = int(self.text1.text())
            # 将text2的输入转换为int类型
            val2 = int(self.text2.text())
            val2 = val1 + val2
            if val2 > 124:
                # 弹出提示框
                reply = QMessageBox.information(self,
                                                "消息",
                                                "请正确输入",
                                                QMessageBox.Ok)
                return
            # 更新
            self.communicate.update_widget.emit(val1, val2)
            # 重画图
            self.widget.repaint()
            # 计算当前块数
            sum = 0
            for i in range(0, len(self.widget.used_val_list), 2):
                sum += self.widget.used_val_list[i + 1] - self.widget.used_val_list[i]
            self.lab7.setText("当前使用块数:" + str(sum))
            self.lab7.setGeometry(30, 170, 230, 20)
            self.lab8.setText("当前剩余块数:" + str(124 - sum))
            self.lab8.setGeometry(200, 170, 230, 20)
            useage = format(float(sum) / float(124) * 100, '.2f')
            self.lab9.setText("当前使用率:" + str(useage) + '%')
            self.lab9.setGeometry(370, 170, 230, 20)

        except:
            # 弹出提示框
            reply = QMessageBox.information(self,
                                            "消息",
                                            "请正确输入",
                                            QMessageBox.Ok)

    # 清空对换区
    def clearValue(self):
        if len(self.widget.used_val_list) == 0:
            # 弹出提示框
            reply = QMessageBox.information(self,
                                            "消息",
                                            "此时对换区为空",
                                            QMessageBox.Ok)
        else:
            #  确认清空?
            reply = QMessageBox.information(self,
                                            "消息",
                                            "是否确认清空对换区",
                                            QMessageBox.Yes | QMessageBox.No)
            if reply != 65536:
                # 清理被使用的列表
                self.widget.used_val_list.clear()
                # 清理被使用的字典
                self.widget.used_dict.clear()
                # 清空颜色列表
                self.widget.color_list = []
                # index变为-1
                self.widget.used_index = -1
                # 重新显示
                self.widget.repaint()
                # 计算当前块数
                sum = 0
                for i in range(0, len(self.widget.used_val_list), 2):
                    sum += self.widget.used_val_list[i + 1] - self.widget.used_val_list[i]
                self.lab7.setText("当前使用块数:" + str(sum))
                self.lab7.setGeometry(30, 170, 230, 20)
                self.lab8.setText("当前剩余块数:" + str(124 - sum))
                self.lab8.setGeometry(200, 170, 230, 20)
                useage = format(float(sum) / float(124) * 100, '.2f')
                self.lab9.setText("当前使用率:" + str(useage) + '%')
                self.lab9.setGeometry(370, 170, 230, 20)
                # 计算当前块数
                sum = 0
                for i in range(0, len(self.widget.used_val_list), 2):
                    sum += self.widget.used_val_list[i + 1] - self.widget.used_val_list[i]
                self.lab7.setText("当前使用块数:" + str(sum))
                self.lab7.setGeometry(30, 170, 230, 20)
                self.lab8.setText("当前剩余块数:" + str(124 - sum))
                self.lab8.setGeometry(200, 170, 230, 20)
                useage = format(float(sum) / float(124) * 100, '.2f')
                self.lab9.setText("当前使用率:" + str(useage) + '%')
                self.lab9.setGeometry(370, 170, 230, 20)

                # 清理写入内容
                self.text1.clear()
                self.text2.clear()

                # 初始化设为True
                self.widget.init_flag = True

                # 弹出提示框
                reply = QMessageBox.information(self,
                                                "消息",
                                                "对换区已清空",
                                                QMessageBox.Ok)
            else:
                pass

    # 格式化
    def file_format(self):
        if len(self.widget2.used_val_list) == 0:
            # 弹出提示框
            reply = QMessageBox.information(self,
                                            "消息",
                                            "此时文件区已格式化",
                                            QMessageBox.Ok)
        else:
            pass
            #  确认清空?
            reply = QMessageBox.information(self,
                                            "消息",
                                            "是否确认格式化文件区",
                                            QMessageBox.Yes | QMessageBox.No)
            if reply != 65536:
                # 清理被使用的列表
                self.widget2.used_val_list.clear()
                # 清理被使用的字典
                self.widget2.used_dict.clear()
                # index变为-1
                self.widget2.used_index = -1
                # 重新显示
                self.widget2.repaint()
                # 计算当前块数
                sum = 0
                for i in range(0, len(self.widget2.used_val_list), 2):
                    sum += self.widget2.used_val_list[i + 1] - self.widget2.used_val_list[i]
                self.lab10.setText("当前使用块数:" + str(sum))
                self.lab10.setGeometry(30, 390, 230, 20)
                self.lab11.setText("当前剩余块数:" + str(900 - sum))
                self.lab11.setGeometry(200, 390, 230, 20)
                useage = format(float(sum) / float(900) * 100, '.2f')
                self.lab12.setText("当前使用率:" + str(useage) + '%')
                self.lab12.setGeometry(370, 390, 230, 20)
                self.widget2.color_list = []

                # 弹出提示框
                reply = QMessageBox.information(self,
                                                "消息",
                                                "文件区已完全格式化",
                                                QMessageBox.Ok)
            else:
                pass

    # 调入文件区
    def to_file(self):
        input = self.widget.used_val_list
        try:
            now = self.widget2.used_val_list[-1]
        except:
            now = 0
        for i in range(0, len(input)):
            input[i] += now

        for i in range(0, len(input), 2):
            if self.widget.init_flag:
                self.widget.color_list = self.widget.color_list[1:]
                self.widget.init_flag = False
            else:
                pass
            # 获取颜色
            color = self.widget.color_list[int(i / 2)]
            # 写入文件区的color_list中
            self.widget2.color_list.append(color)
            # 设置值
            try:
                now = self.widget2.used_val_list[-1]
            except:
                now = 0
            self.widget2.setValue(now, input[i + 1] - input[i] + now)
            # 更新
            self.communicate.update_widget.emit(input[i], input[i + 1])
            # 重画图
            self.widget2.repaint()
            # 计算当前块数
            sum = 0
            for i in range(0, len(self.widget2.used_val_list), 2):
                sum += self.widget2.used_val_list[i + 1] - self.widget2.used_val_list[i]
            self.lab10.setText("当前使用块数:" + str(sum))
            self.lab10.setGeometry(30, 390, 230, 20)
            self.lab11.setText("当前剩余块数:" + str(900 - sum))
            self.lab11.setGeometry(200, 390, 230, 20)
            useage = format(float(sum) / float(900) * 100, '.2f')
            self.lab12.setText("当前使用率:" + str(useage) + '%')
            self.lab12.setGeometry(370, 390, 230, 20)

        # 清理被使用的列表
        self.widget.used_val_list.clear()
        # 清理被使用的字典
        self.widget.used_dict.clear()
        # 清空颜色列表
        self.widget.color_list = []
        # index变为-1
        self.widget.used_index = -1
        # 重新显示
        self.widget.repaint()
        # 计算当前块数
        sum = 0
        for i in range(0, len(self.widget.used_val_list), 2):
            sum += self.widget.used_val_list[i + 1] - self.widget.used_val_list[i]
        self.lab7.setText("当前使用块数:" + str(sum))
        self.lab7.setGeometry(30, 170, 230, 20)
        self.lab8.setText("当前剩余块数:" + str(124 - sum))
        self.lab8.setGeometry(200, 170, 230, 20)
        useage = format(float(sum) / float(124) * 100, '.2f')
        self.lab9.setText("当前使用率:" + str(useage) + '%')
        self.lab9.setGeometry(370, 170, 230, 20)
        # 清理写入内容
        self.text1.clear()
        self.text2.clear()
        return

    # 调入内存
    def to_ram(self):
        if len(self.widget.used_val_list) == 0:
            # 弹出提示框
            reply = QMessageBox.information(self,
                                            "消息",
                                            "此时对换区为空,无法调入内存",
                                            QMessageBox.Ok)
        else:
            data = self.text2.text()
            if int(data)>12:
                # 弹出提示框
                reply = QMessageBox.warning(self,
                                                "消息",
                                                "超过最大内存，无法调入",
                                                QMessageBox.Ok)
            else:

                # 清理被使用的列表
                self.widget.used_val_list.clear()
                # 清理被使用的字典
                self.widget.used_dict.clear()
                # 清空颜色列表
                self.widget.color_list = []
                # index变为-1
                self.widget.used_index = -1
                # 重新显示
                self.widget.repaint()
                # 计算当前块数
                sum = 0
                for i in range(0, len(self.widget.used_val_list), 2):
                    sum += self.widget.used_val_list[i + 1] - self.widget.used_val_list[i]
                self.lab7.setText("当前使用块数:" + str(sum))
                self.lab7.setGeometry(30, 170, 230, 20)
                self.lab8.setText("当前剩余块数:" + str(124 - sum))
                self.lab8.setGeometry(200, 170, 230, 20)
                useage = format(float(sum) / float(124) * 100, '.2f')
                self.lab9.setText("当前使用率:" + str(useage) + '%')
                self.lab9.setGeometry(370, 170, 230, 20)
                # 计算当前块数
                sum = 0
                for i in range(0, len(self.widget.used_val_list), 2):
                    sum += self.widget.used_val_list[i + 1] - self.widget.used_val_list[i]
                self.lab7.setText("当前使用块数:" + str(sum))
                self.lab7.setGeometry(30, 170, 230, 20)
                self.lab8.setText("当前剩余块数:" + str(124 - sum))
                self.lab8.setGeometry(200, 170, 230, 20)
                useage = format(float(sum) / float(124) * 100, '.2f')
                self.lab9.setText("当前使用率:" + str(useage) + '%')
                self.lab9.setGeometry(370, 170, 230, 20)


                # 清理写入内容
                self.text1.clear()
                self.text2.clear()
                self.widget.init_flag = True

                # 弹出提示框
                reply = QMessageBox.information(self,
                                                "消息",
                                                "已调入内存,是否进入内存查看?",
                                                QMessageBox.Yes | QMessageBox.No)
                # 是否进入内存查看
                if reply == 65536:
                    pass
                else:
                    _thread.start_new_thread(new_thread_internal_memory, ("internal_memory", 2, data))


# 主函数
if __name__ == "__main__":
    # 建立新的Qapp
    app = QApplication(sys.argv)
    # 建立Space类
    ex = Space()
    # 退出
    sys.exit(app.exec_())
    print('ok')
