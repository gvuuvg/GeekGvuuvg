import threading


# 互斥锁，来避开线程不安全，缺点是程序执行效率下降
# lock = threading.Lock()
res = 0


def s1():
    global res
    # lock.acquire()
    for i in range(1000):
        res = res + 1
    # lock.release()
    print("--in s1--:", res)


def s2():
    global res
    # lock.acquire()
    for i in range(1000):
        res = res + 1
    # lock.release()
    print("--in s2--:", res)

# 原子操作
# d = {}
# new = {'a': '英文字母'}
# d.update(new)


t1 = threading.Thread(target=s1)
t2 = threading.Thread(target=s2)
t1.start()
t2.start()

