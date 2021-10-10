# dir()
from twilio.rest import Client

class A(object):
    p = "w"

    def q(self):
        """这似乎是一个验证是否是人类的问题"""
        pass


a = A()
print(dir(A))
help(a.q)
print(dir(""))
help("".strip)

s = "  +8618088889999   "
r = s.strip()
print(r)
