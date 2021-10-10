# passwordVerify 密码验证程序

# 1、长度大于8位
def len_check(p):
    return len(p) > 8


# 2、包含大小字母，数字，其他字符中的3种
# 判断一个字符是否是字母使用isalpha，判断一个字符是否是数字使用isdigit
# 判断一个字符是否是大写字母使用 isupper,判断一个字符是否是小写字母使用 islower,
def type_check(p):
    c, n, e, l = 0, 0, 0, 0
    for i in p:
        if i.islower():
            c = 1
        elif i.isupper():
            l = 1
        elif i.isdigit():
            n = 1
        else:
            e = 1

    return c + n + l + e >= 3


# 3、不能有连续长度为3的字串重复 11a211a366
def repeat_check(p):
    n = len(p)
    for i in range(0, n - 3):
        # 如果发现字串重复就返回 False
        if p.count(p[i:i + 3]) > 1:
            return False
    else:
        return True


# print(len_check("12345678"))
# print(type_check("uuuuuu2u"))
# print(repeat_check("11b211a366"))
if __name__ == '__main__':
    while 1:
        pwd = input("请输入密码：")
        if len_check(pwd):
            if type_check(pwd):
                if repeat_check(pwd):
                    print("密码设置成功")
                    break
                else:
                    print("不能有连续长度为3的字串重复")
            else:
                print("至少包含大小字母，数字，其他字符中的3种")
        else:
            print("长度不足9位")