# -*- coding: utf-8 -*-
# @Time    : 2020/11/2 15:57
# @Author  : yangxue
# @Email   : yangxue@xiyun.com.cn
# @File    : sql_handle.py


def sql_handle():
    list=['20110113110064034',
'20110113110064035',
'20110113110064036',
'20110113110064038',
'20110113110064039',
'20110113110064040',
'20110113110064041',
'20110113110064042',
'20110113110064043',
'20110113110064044',
'20110113110064045',
'20110113110064046',
'20110113110064047',
'20110113110064048',
'20110113110064049',
'20110113110064050',
'20110113110064051',
'20110113110064052',
'20110113110064053',
'20110113110064054',
'20110113110064055',
'20110213110064223']
    list1=[]
    list2=[]
    for item in list:

        print('DELETE FROM csr_outstock_bill_detail WHERE detail_id= "%s";'%item)





sql_handle()