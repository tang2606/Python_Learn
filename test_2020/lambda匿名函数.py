# !usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    : lambda匿名函数.py
@Time    : test_2020/4/24 5:02 下午
@Author  : wade.dong
@Email   : wadedong2606@gmail.com
@Software: PyCharm
"""

c = lambda a: a if a else False

def b(a):
    if a:
        return a
    else:
        return False

print(c(0))
print(c(1))
print('*'*60)
print(b(0))
print(b(1))


print('*'*100)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 匿名函数：通过条件表达式，返回最大值
f0 = lambda x,y: x if x> y else y
print(f0(5,10))

# 匿名函数：求三个参数的乘积
f1 = lambda x,y,z: x*y*z
print(f1(1,2,3))

# 缺省的匿名函数
f2 = lambda x,y=2: x+y #使用了默认值
print(f2(10)) #第二个参数为缺省参数，使用默认值2

# 不定长参数的匿名函数
f3 = lambda *z:z #*z返回的是一个元祖
print(f3('hello',False))

# 不定长参数的匿名函数
f4 = lambda **Arg: Arg #arg返回的是一个字典
print(f4(a=1,b=2,k="hello"))


print('*'*100)
'''
匿名函数作为参数使用
'''
def function1(a,b,):
    return a if a>b else b #返回最大值

# 1.定义匿名函数
f0 = lambda b:b*10
# 2.匿名函数作为参数，调用普通函数
function1(100,f0(5))

# 上面两行代码合并为一行
test_01 = function1(10 , (lambda b:b*10)(5))
print(test_01)

