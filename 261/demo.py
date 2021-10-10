import math
class A(object):
    # 私有属性
    __n = '__________a_____________'

    def d(self):
        print(A.__n)

class C(A):
    def bm(self):
        pass


# c = C()
# c.bm()
a = A()
a.d()
