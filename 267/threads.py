import threading
import time

def sing():
    for i in range(6):
        time.sleep(0.5)
        print("唱歌")

def dance():
    for i in range(6):
        time.sleep(0.5)
        print("跳舞")


t1 = threading.Thread(target=sing)
t2 = threading.Thread(target=dance)
t1.start()
t2.start()
