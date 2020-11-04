# -*- coding: utf-8 -*-
# @Time    : 2020/10/29 10:19
# @Author  : yangxue
# @Email   : yangxue@xiyun.com.cn
# @File    : calccostprice.py

from decimal import Decimal

'''
业务模式有3种，采购入库，采购退货出库，销售退货入库
1，采购入库:库存数量（Store），成本价（Costprice）,采购入库数量（Buynum）,不含税采购价（Realprice）
2,采购退货出库：库存数量（Store），成本价（Costprice）,采购退货出库数量（ReturnOutnum）,采购入库时不含税采购价（RealBuyprice）
3,销售退货入库：库存数量（Store），成本价（Costprice）,销售退货入库数量（ReturnInnum）,销售时成本价（BuyCostprice）
公式：
1，fCostprice=(Store*Costprice+Buynum*Realprice)/(Store+Buynum)
2,fCostprice=(Store*Costprice-ReturnOutnum*RealBuyprice)/(Store-ReturnOutnum)
3,fCostprice=(Store*Costprice+ReturnInnum*BuyCostprice)/(Store+ReturnInnum)
'''


class Calculate():
    def __init__(self):
        self.store=float(input('请输入商品库存： '))
        self.costprice=float(input('请输入商品成本价: '))

    def formatdata(self,data):
        fdata=float('%.2f'%data)
        return fdata


    def buysome(self):
        Buynum=float(input('请输入购买数量：'))
        price=float(input('请输入含税采购金额：'))
        tax=float(float(input('请输入税率（）： '))/100.00)
        Realprice=float('%.2f'%(price/(1+tax)))
        taxmoney=float('%.2f'%(price-Realprice))
        fcostprice = float('%.2f'%((self.store * self.costprice + Buynum * Realprice) / (self.store + Buynum)))
        self.store+=Buynum
        self.costprice=fcostprice
        print('不含税采购价：%f,税额为 %f'%(Realprice,taxmoney))
        print('目前库存数量为：%d ,成本价为：%s'%(self.store,self.costprice))

    def returnoutsome(self):
        ReturnOutnum=float(input('请输入退货数量：'))
        RealBuyTaxprice=float(input('请输入采购时含税金额： '))
        tax=float(float(input('请输入税率： '))/100.00)
        RealBuyprice=float('%.2f'%(RealBuyTaxprice/(1+tax)))
        taxmoney=float(RealBuyTaxprice-RealBuyprice)
        fCostprice =float('%.2f'%((self.store*self.costprice-ReturnOutnum*RealBuyprice)/(self.store - ReturnOutnum)))
        self.store=self.store-ReturnOutnum
        self.costprice=fCostprice
        print('不含税采购价：%.2f,税额为 %.2f'%(Realprice,taxmoney))
        print('目前库存数量为：%d ,成本价为：%s' % (self.store, self.costprice))

    def returninsome(self):
        ReturnInnum=float(input('请输入销售退货数量： '))
        BuyCostprice=float(input('请输入销售时成本价： '))
        fcostprice=float('%.2f'%((self.store*self.costprice+ReturnInnum*BuyCostprice)/(self.store+ReturnInnum)))
        self.store+=ReturnInnum
        self.costprice=fcostprice
        print('目前库存数量为：%d ,成本价为：%s' % (self.store, self.costprice))

    def signalCostprice(self):
        tax=float(float(input('请输入税率： '))/100.00)
        RealBuyTaxprice = float(input('请输入销售时含税金额： '))
        x=float(float(input('请输入系数： '))/100.00)
        RealBuyprice = float('%.2f' % (RealBuyTaxprice / (1 + tax)))
        taxmoney = float('%.2f'%(RealBuyTaxprice - RealBuyprice))
        singalcostprice=float('%.2f'%((self.costprice+taxmoney)*(1.00+x)))
        print('不含税单价：%f ,税额：%f'%(RealBuyprice,taxmoney))
        print('成本单价为：',singalcostprice)

    def outcostprice(self):
        pass




    def Do(self):

        while 1:
            y=int(input('请输入业务编号：（采购入库-1，采购退货出库-2，销售退货入库-3，成本单价-4,推出-5）：'))
            if y==1:
                c.buysome()
            elif y ==3:
                c.returninsome()
            elif y ==2:
                c.returnoutsome()
            elif y==4:
                c.signalCostprice()
            elif y==5:
                print('退出')
                break
            else:
                print('输入有误请重新输入！')
                continue


if __name__ =='__main__':
    c=Calculate()
    c.Do()
