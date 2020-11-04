# -*- coding: utf-8 -*-
# @Time    : 2020/9/16 15:05
# @Author  : yangxue
# @Email   : yangxue@xiyun.com.cn
# @File    : jsonpath.py

def data_handle(data, jsonpath):  # 第一次调用这个函数的时候，jsonpath 设为 $. 或$
    if isinstance(data, dict):  #判断数据类型，如果是字典类型执行这个
        for key in data:
            if isinstance(data[key], str) or isinstance(data[key], int):
                jsonpath1 = jsonpath + key
                if key != "jsonpath":
                    print(jsonpath1)  # 这是本次调用该函数可以直接计算出来jsonpath。 这个地方只输出，也可以写到一起txt中

            elif isinstance(data[key], dict):
                jsonpath1 = jsonpath + key + '.'
                data_handle(data[key],jsonpath1)
                # dict1['jsonpath'] = jsonpath1
                # templist.append(dict1)
                # print(templist)
            elif isinstance(data[key], list):
                jsonpath1 = jsonpath + key
                data_handle(data[key], jsonpath1)
    elif isinstance(data, list):  # 第一次jsonpath为  $
        for each in data:
            if isinstance(each, dict):
                jsonpath1 = jsonpath + '[' + str(data.index(each)) + ']' + '.'
                dic2 = {}
                dic2 = each
                dic2['jsonpath'] = jsonpath1
                templist.append(dic2)
            elif isinstance(each, list):
                jsonpath1 = jsonpath + "[" + str(data.index(each)) + "]"
                data_handle(each, jsonpath1)
            elif isinstance(each, str) or isinstance(each, int):
                jsonpath1 = jsonpath + '[' + str(data.index(each)) + ']'
                if each != "jsonpath":
                    print(jsonpath1)
    # for each in templist:
    #     # print(each)
    #     data_handle(each, each['jsonpath'])


data_test={
    "success":True,
    "code":1,
    "msg":"default success",
    "resultObject":{
        "roleId":29,
        "roleNo":"TJS0034",
        "roleName":"123",
        "bizModeId":0,
        "tenantId":0,
        "platformId":2,
        "status":2,
        "creatorId":16,
        "creatorName":"杨雪",
        "createTime":"2020-09-17 09:59:35:000",
        "updateTime":"2020-09-18 14:49:37:000",
        "leafTaskIds":[6,4]
    }
}

data_handle(data_test, "$.")#调用函数传入一个data和一个jsonpath的初始值即可