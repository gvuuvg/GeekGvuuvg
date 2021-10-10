import requests


class Human(object):
    fingers = 10

    def __init__(self, n, a):
        self.name = n
        self.age = a

    def __call__(self, *args, **kwargs):
        pass

    def coding(self):
        print('%s编写了一段程序' % self.name)

    @classmethod
    def dream(cls):
        print('%s做了一场梦' % cls.name)

    @classmethod
    def thinking(cls):
        print(cls.fingers)

    @staticmethod
    def time():
        pass


beijingren = Human("千纸鹤", 12)
print(vars(beijingren))
print(vars(Human))
beijingren()
a = isinstance(beijingren, Human)
print(a)
#
# Human.eyes = 2
# beijingren.dream()
# print(Human.fingers)
# print('修改前', beijingren.fingers)
# beijingren.fingers = 11
# print('修改后', beijingren.fingers)
# print(Human.fingers)
# beijingren.color = 'yellow'
# Human.toe = 15
# lucy = Human('Lucy', 100)
# print(lucy.toe)
# lucy.color = 'white'
# print(lucy.color)
# lucy.dream()
