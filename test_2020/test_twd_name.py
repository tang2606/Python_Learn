

# 导入线程threading模块
import threading
# 导入内置模块time
import time


def prit_name():
    print("my_name.py __name__:", __name__)




def wash_clothes():
    print("洗衣服开始...")
    # sleep 5 秒，默认以秒为单位
    time.sleep(5)
    print("洗衣服完成...")


def clean_room():
    print("打扫房间开始...")
    # sleep 5 秒，默认以秒为单位
    time.sleep(5)
    print("打扫房间完成...")


if __name__ == "__main__":
    # 创建线程并初始化 -- 该线程执行wash_clothes中的代码
    t1 = threading.Thread(target=wash_clothes)
    # 创建线程并初始化 -- 该线程执行clean_room中的代码
    t2 = threading.Thread(target=clean_room)

    t1.start()
    t2.start()