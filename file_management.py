# 导入所需要的包
import sys
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import *
import os
import time
import shutil

global now_path
sys.dont_write_bytecode = True
desktop_path = "./my_os_data/"
now_path = desktop_path

# 创建一个txt文件，文件名为mytxtfile,并向文件写入msg
def text_create(name, msg):
    full_path = now_path + name + '.txt'
    file = open(full_path, 'w')
    file.write(msg)  # msg也就是下面的Hello world!
    # file.close()


# File类
class File(QMainWindow):


    # 初始化
    def __init__(self):
        super(File, self).__init__()
        # 初始化UI
        self.initUI()


    # 初始化UI
    def initUI(self):

        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()


        openfile = QAction('open', self)
        openfile.setStatusTip('open new file')
        openfile.triggered.connect(self.showDialog)


        deletefile = QAction('delete', self)
        deletefile.setStatusTip('delete file')
        deletefile.triggered.connect(self.delete_file)


        savefile = QAction('save', self)
        savefile.setStatusTip('save file')
        savefile.triggered.connect(self.save)


        create_dir = QAction('create', self)
        create_dir.setStatusTip('create dir')
        create_dir.triggered.connect(self.create_dir)


        cd_dir = QAction('cd', self)
        cd_dir.setStatusTip('change dir')
        cd_dir.triggered.connect(self.cd_dir)


        delete_dir = QAction('delete', self)
        delete_dir.setStatusTip('delete dir')
        delete_dir.triggered.connect(self.delete_dir)


        menubar = self.menuBar()
        filemune = menubar.addMenu('$File')
        filemune.addAction(openfile)
        filemune.addAction(savefile)
        filemune.addAction(deletefile)

        filemune = menubar.addMenu('$Dir')
        filemune.addAction(create_dir)
        filemune.addAction(cd_dir)
        filemune.addAction(delete_dir)


        self.setGeometry(450, 100, 500, 500)
        self.setWindowTitle('文件管理系统')
        self.show()


    # 显示文件函数
    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'open file', './my_os_data/')
        if fname[0]:
            try:
                f = open(fname[0], 'r')
                with f:
                    data = f.read()
                    self.textEdit.setText(data)
            except:
                self.textEdit.setText("打开文件失败，可能是文件内型错误")


    # 保存文件函数
    def save(self):
        text, ok = QInputDialog.getText(self, '消息', '输入文件名：')
        if ok and text:

            head = '创建时间:'+time.ctime()+'\n'+'所有者:'+'ly'+'\n'+'文件结构:树形结构'+'\n'+'文件内容：\n'
            data = self.textEdit.toPlainText()

            text_create(text, head+data)
            # 弹出提示框
            reply = QMessageBox.information(self,
                                            "消息",
                                            "保存成功",
                                            QMessageBox.Ok)
        else:
            # 弹出提示框
            reply = QMessageBox.information(self,
                                            "消息",
                                            "请正确输入",
                                            QMessageBox.Ok)


    # 创建dir函数
    def create_dir(self):
        dir_name, ok = QInputDialog.getText(self, '消息', '输入文件夹名：')
        if ok and dir_name:
            os.mkdir(now_path+'/'+dir_name)
            head = '创建时间:'+time.ctime()+'\n'+'所有者:'+'ly'+'\n'+'文件结构:树形结构'+'\n'+'文件内容：\n'

            text_create(dir_name+'/'+dir_name+'_information', head)
            # 弹出提示框
            reply = QMessageBox.information(self,
                                            "消息",
                                            "创建成功",
                                            QMessageBox.Ok)
        else:
            # 弹出提示框
            reply = QMessageBox.information(self,
                                            "消息",
                                            "请正确输入",
                                            QMessageBox.Ok)


    # 进入目录
    def cd_dir(self):
        dir_name, ok = QInputDialog.getText(self, '消息', '输入文件夹名：')
        if ok and dir_name:
            if dir_name=='/':
                # 弹出提示框
                reply = QMessageBox.information(self,
                                                "消息",
                                                "返回根目录成功",
                                                QMessageBox.Ok)
                now = desktop_path
                return
            global now_path
            cd_path = now_path+dir_name
            if os.path.exists(cd_path):
                # 弹出提示框
                reply = QMessageBox.information(self,
                                                "消息",
                                                "进入文件夹成功",
                                                QMessageBox.Ok)

                now_path = cd_path+'/'
                print(cd_path)
            else:
                reply = QMessageBox.information(self,
                                                "消息",
                                                "当前路径不存在该文件夹",
                                                QMessageBox.Ok)
        else:
            # 弹出提示框
            reply = QMessageBox.information(self,
                                            "消息",
                                            "请正确输入",
                                            QMessageBox.Ok)


    # 删除文件
    def delete_file(self):
        text, ok = QInputDialog.getText(self, '消息', '输入文件名：')
        if ok and text:
            print(now_path+text)
            if os.path.exists(now_path+text+'.txt'):
                os.remove(now_path+text+'.txt')
                # 弹出提示框
                reply = QMessageBox.information(self,
                                                "消息",
                                                "删除成功",
                                                QMessageBox.Ok)
            else:
                # 弹出提示框
                reply = QMessageBox.information(self,
                                                "消息",
                                                "文件不存在",
                                                QMessageBox.Ok)
        else:
            # 弹出提示框
            reply = QMessageBox.information(self,
                                            "消息",
                                            "请正确输入",
                                            QMessageBox.Ok)


    # 删除目录
    def delete_dir(self):
        text, ok = QInputDialog.getText(self, '消息', '输入文件夹名：')
        if ok and text:
            print(now_path+text)
            if os.path.exists(now_path+text):
                shutil.rmtree(now_path+text)
                # os.removedirs(now_path+text)
                # 弹出提示框
                reply = QMessageBox.information(self,
                                                "消息",
                                                "删除成功",
                                                QMessageBox.Ok)
            else:
                # 弹出提示框
                reply = QMessageBox.information(self,
                                                "消息",
                                                "文件夹不存在",
                                                QMessageBox.Ok)
        else:
            # 弹出提示框
            reply = QMessageBox.information(self,
                                            "消息",
                                            "请正确输入",
                                            QMessageBox.Ok)


# 主函数
if __name__ == "__main__":
    # 建立app
    app = QApplication(sys.argv)
    # 画出example
    ex = File()
    # 退出
    sys.exit(app.exec_())
