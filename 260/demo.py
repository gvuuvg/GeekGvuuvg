class A(object):
    n = 'a'
    def __init__(self):
        print("A")

    # def bm(self):
    #     print("A bm")

class B(object):
    n = 'b'
    def __init__(self):
        print("B")

    def bm(self):
        print("B bm")


# 多继承
class C(A, B):
    n = 'c'
    def __init__(self):
        print("C")

    def bm(self):
        # 需要直接执行父类里的同名方法，super(),基类，超类，父类
        super().bm()
# 多层继承
class D(C):
    def __init__(self):
        print("D")

# 方法查找顺序 method run/research order
# print(C.__mro__) # C,A,B,object
# c = C()
# print(c.n)
# c.bm()
print(D.__mro__)
# D,C,A,B,object

