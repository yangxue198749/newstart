# -*- coding: utf-8 -*-
# @Time    : 2020/11/2 15:57
# @Author  : yangxue
# @Email   : yangxue@xiyun.com.cn
# @File    : sql_handle.py


def sql_handle():
    list=['20112711910128780',
'20112711910128781',
'20112711910128782',
'20112711910128783',
'20112711910128784',
'20112711910128785']
    list1=['20120311612368540',
'20120311612368541',
'20120311612368542',
'20120311612368543',
'20120311612368544',
'20120311612368545',
'20120311612368546',
'20120311612368547',
'20120311612368548',
'20120311612368549',
'20120311612368550',
'20120311612368551',
'20120311612368552',
'20120311612368553',
'20120311612368554',
'20120311612368555',
'20120311612368556',
'20120311612368557',
'20120311612368558',
'20120311612368559',
'20120311612368560',
'20120311612368561',
'20120311612368562',
'20120311612368563'
    ]
    print('scm详单删除')
    # for item in list:
    #
    #
    #     print('DELETE FROM  sa_sale_outstock_bill_detail  WHERE detail_id= "%s";'%item)
    print('成本还原详单删除')
    for item in list1:

        # print('DELETE FROM  sale_outstock_bill_detail  WHERE detail_id= "%s";'%item)

        # print('UPDATE sale_outstock_bill_detail set real_quantity ="0.00",cost_price="0.000000",cost_amount="0.000000" WHERE detail_id ="%s";'%item)

        print('DELETE FROM  csr_purchase_apply_bill_detail  WHERE detail_id= "%s";' % item)





sql_handle()