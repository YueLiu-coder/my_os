# 导入所需要的包
from thread import *
import _thread
import threadpool


# 主函数
if __name__ == '__main__':
    try:
        print("time:                       thread:")
        _thread.start_new_thread(new_thread_login_desktop, ("login_desktop", 2,))
    except:
        print("Error: 无法启动")
    while 1:
        pass




