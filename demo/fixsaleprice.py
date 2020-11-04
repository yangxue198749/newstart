# -*- coding: utf-8 -*-
# @Time    : 2020/9/28 14:49
# @Author  : yangxue
# @Email   : yangxue@xiyun.com.cn
# @File    : fixsaleprice.py


import requests
import json
import os
import xlrd
# from . import tool_readxls
import demo.tool_readxls

class Fixsaleprice:
    def __init__(self):
        self.base_url='https://xybppre.xiyunfin.com/'
        self.server='xybp/ba/user/login'
        self.loginurl=os.path.join(self.base_url,self.server)
        self.headers={'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
                      'Content-Type': 'application/json'}
        self.datafile=r"C:\Users\Think\Documents\WeChat Files\wxid_b0uruuqqfid421\FileStorage\File\2020-09\石家庄集采销售价格审批表（钉钉更新售价使用）(4)(2)_142(1)(1)(2).xlsx"
        self.tablename="Sheet3"
        self.logindata={}
        self.logindata['account']='yangxue'
        self.logindata['password']='y123456'
        self.logindata['force']=1
        self.loginres=requests.post(url=self.loginurl,data=json.dumps(self.logindata),headers=self.headers).json()
        self.headers['authorization']=self.loginres['resultObject']['token']



    def get_xlsx_data(self):

        self.r=demo.tool_readxls.ExcelData(self.datafile,self.tablename)
        self.data=self.r.readExcel()
        return self.data




    def data_get_materialname(self):
        data=self.get_xlsx_data()
        self.materialnamelist=[]
        self.baseserver='xybp/ma/material/page'
        self.url=os.path.join(self.base_url,self.baseserver)
        self.params={}
        self.params['pageSize']=10
        self.params['currentPage'] = 1
        self.params['materialName'] = None
        self.params['brandId'] = None
        self.params['status'] = None
        self.params['totalCount'] =0
        for item in data:
            self.params['materialNo']=item['商品编码']
            # print(self.params)
            self.res=requests.get(url=self.url,params=self.params,headers=self.headers).json()

            materialnam=self.res['resultObject']['pageData'][0]['materialName']
            self.materialnamelist.append(materialnam)


    def get_salepriceId(self):
        self.data_get_materialname()
        self.salepriceId=[]
        materialdata = {}
        self.server='xybp/related/party/price/page'
        self.url=os.path.join(self.base_url,self.server)
        self.params={}
        self.params['pageSize']=10
        self.params['currentPage']=1
        self.params['totalCount']=0
        self.params['customerName']=None
        self.params['warehouseName']='石家庄集采仓'
        for item in self.materialnamelist:

            self.params['materialName']=item

            self.res=requests.get(url=self.url,params=self.params,headers=self.headers).json()

            if self.res['resultObject']['pageData']:
                materialdata['salepriceId']=self.res['resultObject']['pageData'][0]['salePriceId']
                materialdata['materialNo']=self.res['resultObject']['pageData'][0]['materialNo']
                materialdata['gsoNo']=self.res['resultObject']['pageData'][0]['gsoNo']
                materialdata['warehouseNo']=self.res['resultObject']['pageData'][0]['warehouseNo']
                self.salepriceId.append(materialdata)

    def get_salepricecontent(self):
        self.get_salepriceId()
        self.salepricecontent=[]
        self.server='xybp/related/party/price/detail'
        self.url=os.path.join(self.base_url,self.server)
        self.params = {}
        for item in self.salepriceId:
            self.params['salePriceId'] = item['salepriceId']
            self.params['materialNo'] = item['materialNo']
            self.params['gsoNo'] = item['gsoNo']
            self.params['warehouseNo'] = item['warehouseNo']
            self.res=requests.get(url=self.url,params=self.params,headers=self.headers).json()
            self.salepricecontent.append(self.res['resultObject'])
        # print(self.salepricecontent)

    def changesaleprice(self):
        # self.datatochangelist=[]
        self.data=self.get_salepricecontent()
        # print(self.salepricecontent,type(self.salepricecontent))
        self.server = 'xybp/related/party/price/update'
        self.url = os.path.join(self.base_url, self.server)
        print(self.url)
        for content in self.salepricecontent:
            for item in content['relatedPartyPriceDetailList']:
                # print(item)
                '''在这里修改一下价格'''
                item['saleTaxPrice']=16
                # print('after----',item)
            self.res=requests.post(url=self.url,data=json.dumps(content),headers=self.headers).json()
            print(self.res)

        # print(self.salepricecontent)






f=Fixsaleprice()
# f.data_get_materialname()
# f.get_salepriceId()
# f.get_salepricecontent()
f.changesaleprice()