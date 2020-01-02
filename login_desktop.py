import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import _thread
import os
from thread import *


# 创建主窗口
class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('Desktop')
        self.setFixedSize(self.width(), self.height())


        # 设置按钮btn1
        self.btn1 = QPushButton(self)
        # 设置按钮btn1的名字
        self.btn1.setText("磁盘")
        # 定位按钮btn1的位置
        self.btn1.setGeometry(20, 30, 70, 70)

        # 设置按钮btn2
        self.btn2 = QPushButton(self)
        # 设置按钮btn2的名字
        self.btn2.setText("内存")
        # 定位按钮btn2的位置
        self.btn2.setGeometry(20, 130, 70, 70)

        # 设置按钮btn3
        self.btn3 = QPushButton(self)
        # 设置按钮btn3的名字
        self.btn3.setText("文件")
        # 定位按钮btn3的位置
        self.btn3.setGeometry(20, 230, 70, 70)
        # 设置按钮btn4
        self.btn4 = QPushButton(self)
        # 设置按钮btn4的名字
        self.btn4.setText("关机")
        # 定位按钮btn4的位置
        self.btn4.setGeometry(250, 330, 150, 20)



        # 连接打开磁盘函数
        self.btn1.clicked.connect(self.open_external_memory)


        # 连接打开内存函数
        self.btn2.clicked.connect(self.open_internal_memory)


        # 连接打开内存函数
        self.btn3.clicked.connect(self.open_file)


        # 连接关机函数
        self.btn4.clicked.connect(self.shutdown)


    # 打开磁盘函数
    def open_external_memory(self):
        try:
            _thread.start_new_thread(new_thread_external_memory, ("external_memory", 2,))
        except:
            print("Error: 无法启动")


    # 打开内存函数
    def open_internal_memory(self):
        try:
            _thread.start_new_thread(new_thread_internal_memory_open, ("internal_memory", 2,))
        except:
            print("Error: 无法启动")


    # 打开文件函数
    def open_file(self):
        try:
            _thread.start_new_thread(new_thread_file, ("file_management", 2,))
        except:
            print("Error: 无法启动")


    # 关机函数
    def shutdown(self):
        # 弹出提示框
        reply = QMessageBox.information(self,
                                        "消息",
                                        "确定关闭计算机?",
                                        QMessageBox.Yes|QMessageBox.No)
        if reply == 65536:
            pass
        else:
            # 关闭
            self.destroy()


# 对话框
class logindialog(QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('MY_OS登录')
        self.resize(150, 130)
        self.setFixedSize(self.width(), self.height())
        self.setWindowFlags(Qt.WindowCloseButtonHint)

        # 设置界面控件
        self.frame = QFrame(self)
        self.verticalLayout = QVBoxLayout(self.frame)

        self.lineEdit_account = QLineEdit()
        self.lineEdit_account.setPlaceholderText("请输入账号")
        self.verticalLayout.addWidget(self.lineEdit_account)

        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setPlaceholderText("请输入密码")
        self.verticalLayout.addWidget(self.lineEdit_password)

        self.pushButton_enter = QPushButton()
        self.pushButton_enter.setText("确定")
        self.verticalLayout.addWidget(self.pushButton_enter)

        self.pushButton_quit = QPushButton()
        self.pushButton_quit.setText("取消")
        self.verticalLayout.addWidget(self.pushButton_quit)

        # 连接按钮事件
        self.pushButton_enter.clicked.connect(self.on_pushButton_enter_clicked)
        self.pushButton_quit.clicked.connect(QCoreApplication.instance().quit)


    def on_pushButton_enter_clicked(self):
        # 账号判断 密码判断
        if self.lineEdit_account.text() == "" and self.lineEdit_password.text() == "":

            # 通过验证，关闭对话框并返回1
            self.accept()
            # 弹出提示框
            reply = QMessageBox.information(self,
                                            "消息",
                                            "登录成功,欢迎来到MY_OS",
                                            QMessageBox.Ok)
        else:
            # 弹出提示框
            reply = QMessageBox.information(self,
                                            "消息",
                                            "登录失败",
                                            QMessageBox.Ok)


# 主函数
if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = logindialog()
    if  dialog.exec_()==QDialog.Accepted:
        the_window = MainWindow()
        the_window.show()
        sys.exit(app.exec_())
