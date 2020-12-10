# -*- coding: utf-8 -*-
# @Time    : 2020/11/24 9:22
# @Author  : yangxue
# @Email   : yangxue@xiyun.com.cn
# @File    : learn.py

#快速的生成一个0-100的列表
# print(list(range(0,100)))
# 一行代码实现0,100之和
print(sum(range(0,100)))

#3，改变全局变量
a=5

def show():
    global a
    a=2


# print(list(range(5,19)))
# #
# # list1=[5, 6, 7, 8, 9, 10, 11, 12, 13, 6, 7,8, 9, 11]
# # a=set(list1)
# # print(a,type(a))
# # a=[i for i in a]
# # print(a,type(a))

# map用法
# list2=[1,2,3,4,5]
# def fn(x):
#     return x**2
#
# b=map(fn,list2)
# b=[i for i in b if i>10]
# print(b)

# 生成随机小数

# import random
# import numpy as np
#
# print(random.randint(0,9))
# print(random.randrange(0,10,2))
# print(np.random.rand(5))
# print(random.random())

# shengchengyigessuijiyanzhengma

# def check_num():
#     import random
#     import numpy as np
#     seed='0123456789'
#     check_num=[]
#     for i in range(4):
#         check_num.append(random.choice(seed))
#     print(check_num)
#
# check_num()

# s='adsfhasdfgadfgsasgd'
# res=set(s)
# print(res)
# res=list(res)
# print(res)
# res.sort(reverse=False)
# res=''.join(res)
# print(res)

dict1={'name':'yan',"age":19,'sex':'man'}
# dict2={'name':'yan','age':18,'sex':'woman'}
# dict3={'school':'hi'}
# # 方式一 pop+key
# dict1.pop('name')
# dict1['name']='yy'
# print(dict1)
# # 方式二 del
# del dict1['name']
# print(dict1)
# # 合并字典 如果key 相同则覆盖 不同则增加
# dict1.update(dict2)
# dict2.update(dict3)
# print(dict1)
# print(dict2)
#
# list1=sorted(dict1.items(),key=lambda i:i[0],reverse=False)
# print(list1)
# new_dict={}
# for i in list1:
#     new_dict[i[0]]=i[1]

# print(new_dict)
#  '''
#  1生成一个列表，步数为2  [5, 7, 9, 11, 13, 15, 17]
#  2，用set去重，转成了set类型对象   {5, 7, 9, 11, 13, 15, 17} <class 'set'>
#  3，用列表生成式，把set对象转成列表     [5, 7, 9, 11, 13, 15, 17] <class 'list'>
#  '''
# list1=list(range(5,19,2))
# print(list1)
# res=set(list1)
# print(res,type(res))
# res=[i for i in res]
# print(res,type(res))

# list3=[1, 2, 3, 4, 5, 6, 7, 8, 9]
# def fn(x):
#     return x%2==1
#
#
# new_list=filter(fn,list3)
# new_list=[i for i in new_list]
# print(new_list)
#
# list4=[6,5,2,2]
# list5=[1,9,7,8]
# list4.extend(list5)
# list4.sort(reverse=False)
# print(list4)

# import os,sys
# base_dir=os.path.realpath(__file__)
# dir1=os.path.split(base_dir)
# dir=os.path.join(dir1[0],'haha')
#
# print(dir)

# glist=(i for i in range(10))
#
# for j in range(5):
#     n=glist.next()
#     print(n)

# l=[[1,2],[3,4],[5,6]]
# list1=[j for i in l for j in i ]
# print(list1)

# dict1={'name':'yangxue','age':18}
import collections

# a=')((aadg)(jnvh)'
# n=1
# dict1={}
# l=collections.Counter(a)
# if l['(']==l[')']:
#     if a.rfind('(')>a.rfind(')'):
#         for i in a:
#             if i=='(':
#                 dict1['%d'%n]=')'
#                 n+=1
#             elif i==')':
#                 n-=1
#                 dict1.pop('%d'%n)
#             else:
#                 print('go')
#     else:
#         print('括号结尾在前，开始在后')
# else:
#     print('括号对数错误')


import heapq
import collections

a='())(((aadg)(jnvh))'
heap=[]
l=collections.Counter(a)
#如果左括号和右括号出现次数不一致，直接返回不一致
if l['(']==l[')']:
    print(a.find('('),a.find(')'))
    # 如果第一个右括号在第一个左括号后，最后一个优酷号在左括号后，满足条件
    if a.find('(')<a.find(')') and a.rfind('(') > a.rfind(')'):
        for i in a:
            # 如果是左括号，压栈，把左括号压到栈中
            if i=='(':
               heapq.heappush(heap,i)
               print(heap)
            # 如果是右括号并且栈里不是空，弹栈
            elif i==')' and len(heap)>0:
               heapq.heappop(heap)
               print(heap)
            # 如果是右括号并且栈里是空，括号位置有问题
            elif i==')' and len(heap)==0:
                print('括号不是成对出现')
            #其他字符直接过
            else:
                pass

    else:
        print('括号位置不对')
else:
    print('括号对数错误')
#
#
# t=('a','b','c','d','e')
# t1=(1,2,3,4,5)
#
# res=zip(t,t1)
# a0=dict(res)
# print(list(res))
#
# res=[a0[s] for s in a0]
# print(res)