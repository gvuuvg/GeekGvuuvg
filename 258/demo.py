from collections.abc import Iterable

# 实例isinstance
# help(isinstance)
b = []
a = isinstance(b, Iterable)
print(a)
print(isinstance(0, int))
print(isinstance(False, int))
# callable

c = lambda x,y:x+y
print(c(1,2))
print(callable(1))
# help
help(callable)

def f():
    """这是一个函数"""
    pass
help(Iterable)
print(dir(""))
help("".isupper)

# id
aa = '1'
bb = '1'
print(id(aa), id(bb))
aa = '2'
print(id(aa), id(bb))
# vars
print(vars(list))
