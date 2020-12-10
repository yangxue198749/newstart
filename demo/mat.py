# -*- coding: utf-8 -*-
# @Time    : 2020/12/2 10:49
# @Author  : yangxue
# @Email   : yangxue@xiyun.com.cn
# @File    : mat.py

import matplotlib.pyplot as mlp
from newstart.demo.tool_readxls import *

#
# mlp.figure(3,dpi=200)
#
# mlp.subplot(3,3,1)
# mlp.subplot(3,3,2)
# mlp.subplot(3,3,3)
# mlp.subplot(3,3,4)
#
# mlp.show()

e=ExcelData('D:\downloads\data.xlsx','Sheet1')
res=e.readExcel()
print(res[0])
listsku=[]
# for item in res:
#     listsku.append(item.get('商品编码'))

[listsku.append(item.get('商品编码')) for item in res]

print(set(listsku))