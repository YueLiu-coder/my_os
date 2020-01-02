import _thread
import time
import os
# 执行内存线程函数
def new_thread_internal_memory(threadName, delay, para=''):
    print ("%s    %s" % (time.ctime(), threadName))
    os.system('python '+threadName+'.py '+para)

# 执行内存线程函数
def new_thread_internal_memory_open(threadName, delay):
    print ("%s    %s" % (time.ctime(), threadName))
    os.system('python '+threadName+'.py')

# 执行外存线程函数
def new_thread_external_memory(threadName, delay, para=''):
    print ("%s    %s" % (time.ctime(), threadName))
    os.system('python '+threadName+'.py '+para)

# 执行文件线程函数
def new_thread_file(threadName, delay, para=''):
    print ("%s    %s" % (time.ctime(), threadName))
    os.system('python '+threadName+'.py '+para)

# 执行登录线程函数
def new_thread_login_desktop(threadName, delay, para=''):
    print ("%s    %s" % (time.ctime(), threadName))
    os.system('python '+threadName+'.py '+para)