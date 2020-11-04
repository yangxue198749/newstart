# -*- coding: utf-8 -*-
# @Time    : 2020/10/22 10:40
# @Author  : yangxue
# @Email   : yangxue@xiyun.com.cn
# @File    : sing3.py

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
    print(private_key)
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




privateKey='MIICWwIBAAKBgQCP7oHI9EWfQtGgGaFhhYZ8HgTZrWG3yAJAl4u8Xrk9svdbRKYX/41vgPW29T0yFVJKTrFIW4fnLquFR3l2uLJdbEWzE26bZLrS6N8gYn9ydqlCh3Vv1pRuoTrgymG04+FsB+cNQB1TYgnhFmwtkakbluwLmmdPdiT8Bhuw+aOXGQIDAQABAoGAJRvoSGh6ftpac73H9v3XM68Frx3dwOWHdyHbfECr3/WBgv2LGUrhK2uDbp2CHqSSp+fsG2zF+Fv3CxDnhy2NhtcnoOek53CzoAoNKlJ0BTRE7A0RbwhQ4WDbKDnB4WJAYhKiiUIiQSavabX2tn8o0MpdYFRweuKKAZUaow5J82UCQQDWk/vrKPDEHoJnubxoEN7hdNL2vg8/BC47CM1BPUo/AVJixAalld/XkmjdBtQGkDOcQiE+iqDOQG4Cfdhzx3TzAkEAq7dR/hSfaCDLn5C9/m0wFZbZcB632SbeVU9JFEyQRrPiwQzYzu1lQThUvFn29dBCfHjBnyI3+xJDJzt8TVz2wwJAL+TwAdkthFja+pP2fbPmS6Rrwi9B7+ra9spMJhesDswYu3rNkQAW6mL/jPYNNTnSizoneXIv2ll/NIcqXQ1UCQJABYypI7L669yTeBavbTeOJER5xnvXqTbuXIdxbyyCRSavH1oQ768QZKkzY9rsdklCvM8SQthSQtT2QqBThhSJDQJAdWPCDlwOAklGGn3H4Cum1kgIssvhSnCMW1AzCXUuSzMZkCs5iegggexIvHmnG5Sb7pzwARJXR4IrdALWZZ8Lpw=='
cont="a=jajgdajsgjajsgkljalskdjhglk".encode('utf-8')
c=sign(cont,privateKey,'RSA2')
print(c)