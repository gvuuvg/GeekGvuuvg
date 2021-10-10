# 多线程扫描磁盘，最后将扫描文件的总数打印出来
import os
import threading

res = 0


def scan(pa="C:/"):
    global res
    r = os.listdir(pa)
    for i in r:
        # 判断是文件还是文件夹
        temp_path = pa + "/" + i
        if os.path.isdir(temp_path):
            try:
                scan(temp_path)
            except (PermissionError, FileNotFoundError):
                continue
        file_info = os.stat(temp_path)
        num = file_info.st_size / 1024 / 1024
        if num > 1:
            res += 1
            print("文件名：%s,大小为%0.2f %s" % (temp_path, num, "MB") + "\n")


if __name__ == '__main__':
    ct = threading.Thread(target=scan, args=("E:/GISqTransfer",))
    dt = threading.Thread(target=scan, args=("E:/py",))
    et = threading.Thread(target=scan, args=("E:/repository",))
    ct.start()
    dt.start()
    et.start()
    # join
    ct.join()
    dt.join()
    et.join()
    print('扫描到%d个大于10M的文件' % res)
