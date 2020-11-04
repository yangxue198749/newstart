# -*- coding: utf-8 -*-
# @Time    : 2020/9/27 10:49
# @Author  : yangxue
# @Email   : yangxue@xiyun.com.cn
# @File    : sing2.py


from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import MD5,SHA,SHA1
import base64
import time
import requests
# from . import sing3
import rsa
import base64

__pem_begin = '-----BEGIN RSA PRIVATE KEY-----\n'
__pem_end = '\n-----END RSA PRIVATE KEY-----'


def sign(content, private_key, sign_type):
    """签名

    :param content: 签名内容
    :type content: str

    :param private_key: 私钥字符串，PKCS#1
    :type private_key: str

    :param sign_type: 签名类型，'RSA', 'RSA2'二选一
    :type sign_type: str

    :return: 返回签名内容
    :rtype: str
    """
    if sign_type.upper() == 'RSA':
        return rsa_sign(content, private_key, 'SHA-1')
    elif sign_type.upper() == 'RSA2':
        return rsa_sign(content, private_key, 'SHA-256')
    else:
        raise Exception('sign_type错误')


def rsa_sign(content, private_key, _hash):
    """SHAWithRSA

    :param content: 签名内容
    :type content: str

    :param private_key: 私钥
    :type private_key: str

    :param _hash: hash算法，如：SHA-1,SHA-256
    :type _hash: str

    :return: 签名内容
    :rtype: str
    """
    private_key = _format_private_key(private_key)
    pri_key = rsa.PrivateKey.load_pkcs1(private_key.encode('utf-8'))
    sign_result = rsa.sign(content, pri_key, _hash)
    return base64.b64encode(sign_result)


def _format_private_key(private_key):
    """对私进行格式化，缺少"-----BEGIN RSA PRIVATE KEY-----"和"-----END RSA PRIVATE KEY-----"部分需要加上

    :param private_key: 私钥
    :return: pem私钥字符串
    :rtype: str
    """
    if not private_key.startswith(__pem_begin):
        private_key = __pem_begin + private_key
    if not private_key.endswith(__pem_end):
        private_key = private_key + __pem_end
    return private_key


formattime=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())

params={"format":"JSON",
    "charset":"utf-8",
    "sign_type":"RSA",
    "sign":"fyTffsJFd4rWWKFHV4oBB9rwYMh9h02INGLDCsNbAD38vZIClyVBbwERCK8/HlMZXr0K9nYuNkE9xVKOCDvNkStfVku9Fe7lCzzMhDovv+wKnIc0LML+ujgg3H19Ywu5OjgmM6qrSDtW7oykeEWNreAyw9UwXUeZNYzfIyVZDu2uw/cFlxRmKKPiOYMwHP53dmPz84Hez7WQHwjEcqrqRzjHlzB/+LRsan5CCzd1mqTh5UjYBN/bKNLrqmhvBofXh6Hsb9h+T7CnKbHzVRDiMTYNSRxzwf/4U3n2cbHacpm+cyFE3WJkkOv5AhViPtWc7FW3PQ8tbQeDUOYE5xgELw==",
    "timestamp":'2020-10-22 15:18:48',
    "version":"1.0",
    "app_auth_token":"45e4ea97-c0a6-4872-86ad-3438dfa0e735",
    "app_key":"c2c3ab6154fb494a8ec453a08a41eb2c",
    "biz_content":{
        "group_one_no":"01",
        "group_two_no":"01.01",
        "org_no":"113560118",
        "start_time":"2020-07-24 03:07:50",
        "end_time":"2020-08-24 03:07:50",
        "query_page":False,
        "current_page":1,
        "page_size":10
    }
}

def RSA_sign(encrData):
    privateKey = 'MIICWwIBAAKBgQCP7oHI9EWfQtGgGaFhhYZ8HgTZrWG3yAJAl4u8Xrk9svdbRKYX/41vgPW29T0yFVJKTrFIW4fnLquFR3l2uLJdbEWzE26bZLrS6N8gYn9ydqlCh3Vv1pRuoTrgymG04+FsB+cNQB1TYgnhFmwtkakbluwLmmdPdiT8Bhuw+aOXGQIDAQABAoGAJRvoSGh6ftpac73H9v3XM68Frx3dwOWHdyHbfECr3/WBgv2LGUrhK2uDbp2CHqSSp+fsG2zF+Fv3CxDnhy2NhtcnoOek53CzoAoNKlJ0BTRE7A0RbwhQ4WDbKDnB4WJAYhKiiUIiQSavabX2tn8o0MpdYFRweuKKAZUaow5J82UCQQDWk/vrKPDEHoJnubxoEN7hdNL2vg8/BC47CM1BPUo/AVJixAalld/XkmjdBtQGkDOcQiE+iqDOQG4Cfdhzx3TzAkEAq7dR/hSfaCDLn5C9/m0wFZbZcB632SbeVU9JFEyQRrPiwQzYzu1lQThUvFn29dBCfHjBnyI3+xJDJzt8TVz2wwJAL+TwAdkthFja+pP2fbPmS6Rrwi9B7+ra9spMJhesDswYu3rNkQAW6mL/jPYNNTnSizoneXIv2ll/NIcqXQ1UCQJABYypI7L669yTeBavbTeOJER5xnvXqTbuXIdxbyyCRSavH1oQ768QZKkzY9rsdklCvM8SQthSQtT2QqBThhSJDQJAdWPCDlwOAklGGn3H4Cum1kgIssvhSnCMW1AzCXUuSzMZkCs5iegggexIvHmnG5Sb7pzwARJXR4IrdALWZZ8Lpw=='
    private_keyBytes = base64.b64decode(privateKey)
    priKey = RSA.importKey(private_keyBytes)
    #priKey = RSA.importKey(privateKey)
    signer = PKCS1_v1_5.new(priKey)

    hash_obj = SHA1.new(encrData.encode('utf-8'))
    signature = base64.b64encode(signer.sign(hash_obj))
    return signature

# e=RSA_sign(params)
# params['sign']=e.decode(encoding='utf-8')


def verify(signature,encrData):
    publicKey = 'MIICWwIBAAKBgQCP7oHI9EWfQtGgGaFhhYZ8HgTZrWG3yAJAl4u8Xrk9svdbRKYX/41vgPW29T0yFVJKTrFIW4fnLquFR3l2uLJdbEWzE26bZLrS6N8gYn9ydqlCh3Vv1pRuoTrgymG04+FsB+cNQB1TYgnhFmwtkakbluwLmmdPdiT8Bhuw+aOXGQIDAQABAoGAJRvoSGh6ftpac73H9v3XM68Frx3dwOWHdyHbfECr3/WBgv2LGUrhK2uDbp2CHqSSp+fsG2zF+Fv3CxDnhy2NhtcnoOek53CzoAoNKlJ0BTRE7A0RbwhQ4WDbKDnB4WJAYhKiiUIiQSavabX2tn8o0MpdYFRweuKKAZUaow5J82UCQQDWk/vrKPDEHoJnubxoEN7hdNL2vg8/BC47CM1BPUo/AVJixAalld/XkmjdBtQGkDOcQiE+iqDOQG4Cfdhzx3TzAkEAq7dR/hSfaCDLn5C9/m0wFZbZcB632SbeVU9JFEyQRrPiwQzYzu1lQThUvFn29dBCfHjBnyI3+xJDJzt8TVz2wwJAL+TwAdkthFja+pP2fbPmS6Rrwi9B7+ra9spMJhesDswYu3rNkQAW6mL/jPYNNTnSizoneXIv2ll/NIcqXQ1UCQJABYypI7L669yTeBavbTeOJER5xnvXqTbuXIdxbyyCRSavH1oQ768QZKkzY9rsdklCvM8SQthSQtT2QqBThhSJDQJAdWPCDlwOAklGGn3H4Cum1kgIssvhSnCMW1AzCXUuSzMZkCs5iegggexIvHmnG5Sb7pzwARJXR4IrdALWZZ8Lpw=='
    public_keyBytes = base64.b64decode(publicKey)
    pubKey = RSA.importKey(public_keyBytes)
    #pubKey = RSA.importKey(publicKey)
    h = MD5.new(encrData.encode('utf-8'))
    verifier = PKCS1_v1_5.new(pubKey)
    return verifier.verify(h, base64.b64decode(signature))
d = sorted(params.items(), key=lambda x: x[0])
list_l = []
for i in range(len(d)):
    k, v = d[i]
    if i == 0:
        str1 = k + "=" + v
        list_l.append(str1)
    else:
        str2 = "&" + str(k) + "=" + str(v)
        list_l.append(str2)
        content = ''.join([str(i) for i in list_l])

cont='app_auth_token'+'='+params['app_auth_token']+'&app_key'+'='+params['app_key']+'&timestamp'+'='+params['timestamp']+'&version'+'='+params['version']+'&format'+'='+params['format']+'&biz_content'+'='+str(params['biz_content'])+'&sign_type'+'='+params['sign_type']
print(content)
#e='fyTffsJFd4rWWKFHV4oBB9rwYMh9h02INGLDCsNbAD38vZIClyVBbwERCK8/HlMZXr0K9nYuNkE9xVKOCDvNkStfVku9Fe7lCzzMhDovv+wKnIc0LML+ujgg3H19Ywu5OjgmM6qrSDtW7oykeEWNreAyw9UwXUeZNYzfIyVZDu2uw/cFlxRmKKPiOYMwHP53dmPz84Hez7WQHwjEcqrqRzjHlzB/+LRsan5CCzd1mqTh5UjYBN/bKNLrqmhvBofXh6Hsb9h+T7CnKbHzVRDiMTYNSRxzwf/4U3n2cbHacpm+cyFE3WJkkOv5AhViPtWc7FW3PQ8tbQeDUOYE5xgELw=='
# e=sign(content.encode('utf-8'),privateKey,'RSA')
e=RSA_sign(content)

# params['sign']=e.decode(encoding='utf-8')
params['sign']='fyTffsJFd4rWWKFHV4oBB9rwYMh9h02INGLDCsNbAD38vZIClyVBbwERCK8/HlMZXr0K9nYuNkE9xVKOCDvNkStfVku9Fe7lCzzMhDovv+wKnIc0LML+ujgg3H19Ywu5OjgmM6qrSDtW7oykeEWNreAyw9UwXUeZNYzfIyVZDu2uw/cFlxRmKKPiOYMwHP53dmPz84Hez7WQHwjEcqrqRzjHlzB/+LRsan5CCzd1mqTh5UjYBN/bKNLrqmhvBofXh6Hsb9h+T7CnKbHzVRDiMTYNSRxzwf/4U3n2cbHacpm+cyFE3WJkkOv5AhViPtWc7FW3PQ8tbQeDUOYE5xgELw=='
# print(e)

headers={'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
            'Content-Type': 'application/json'}
r=requests.get(url='http://t1101.xyscm-customer.yunzong:11370/open/material/materials',params=params,headers=headers).json()
print(r)
