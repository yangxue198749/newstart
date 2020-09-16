# -*- coding: utf-8 -*-
# @Time    : 2020/9/16 15:05
# @Author  : yangxue
# @Email   : yangxue@xiyun.com.cn
# @File    : jsonpath.py

def data_handle(data, jsonpath):  # 第一次调用这个函数的时候，jsonpath 设为 $. 或$
    templist = []  # 把为字典的value 都放在这里。  这是一个  [{...,jsonpath:jsonpath}]
    if isinstance(data, dict):  # 第一次jsonpath为 $.
        # print("111")
        for key in data:
            if isinstance(data[key], str) or isinstance(data[key], int):
                # print("22")
                jsonpath1 = jsonpath + key
                if key != "jsonpath":
                    print(jsonpath1)  # 这是本次调用该函数可以直接计算出来jsonpath。 这个地方只输出，也可以写到一起txt中

            elif isinstance(data[key], dict):
                dict1 = {}
                dict1 = data[key]
                jsonpath1 = jsonpath + key + '.'
                dict1['jsonpath'] = jsonpath1
                templist.append(dict1)
                print(templist)
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
    for each in templist:
        # print(each)
        data_handle(each, each['jsonpath'])


data_test={
    "success":True,
    "code":1,
    "msg":"default success",
    "resultObject":{
        "accountVO":{
            "accountId":3,
            "account":"yangxue",
            "accountType":2,
            "name":"杨雪",
            "phone":"13566009900",
            "gsoGroupId":1,
            "gsoGroupNo":"001",
            "gsoGroupName":"千禧优选供应链事业群",
            "gsoSubjectId":57,
            "gsoSubjectNo":"001.203",
            "gsoSubjectName":"禧云世纪供应链管理（天津）有限公司",
            "gsoOrganizationId":88,
            "gsoOrganizationNo":"001.203.104",
            "gsoOrganizationName":"临汾集采",
            "warehouseId":0,
            "warehouseNo":"",
            "warehouseName":"",
            "status":2,
            "bizModeId":0,
            "tenantId":0,
            "platformId":2,
            "platformNumber":"2",
            "platformName":"运营中台_管理平台"
        },
        "token":"1fd74b114bdb4eeca5dbbb624588433a",
        "platform":2
    }
}
data_handle(data_test, "$.")#调用函数传入一个data和一个jsonpath的初始值即可