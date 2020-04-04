"""
    @File: SmsByAli.py
    @Type: function -> (custom)
    @Description: 使用Ali的短信SDK发送短信

    @Author: Leobod
    @Version: 1.0.0
    @Modify Time: 2020-02-19

    @Contract: leobod@eside.cn
    @License: ©2019-2020 leobod 苏ICP备17004905号
"""

import json
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest

from bmpentry.BMPConst.AliConst import ALIYUN_SETTINGS, ALIYUN_SMS_ACTION

# 加载Client
def initClient():
    client = AcsClient(
        ALIYUN_SETTINGS["access"]["accessKeyId"],
        ALIYUN_SETTINGS["access"]["accessSecret"],
        ALIYUN_SETTINGS["access"]["RegionId"]
    )
    return client

# 设置Sms的头部信息
def initSmsHeader():
    request = CommonRequest()
    request.set_accept_format(ALIYUN_SETTINGS["sms"]["accept_format"])
    request.set_domain(ALIYUN_SETTINGS["sms"]["domain"])
    request.set_method(ALIYUN_SETTINGS["sms"]["method"])
    request.set_protocol_type(ALIYUN_SETTINGS["sms"]["protocol_type"]) # https | http
    request.set_version(ALIYUN_SETTINGS["sms"]["version"])
    return request

# 包装Sms的参数
def initSmsParameter(phone, code):
    request = initSmsHeader()
    request.set_action_name(ALIYUN_SMS_ACTION["sendsms"]["name"])
    request.add_query_param('RegionId', ALIYUN_SETTINGS["access"]["RegionId"])
    request.add_query_param('PhoneNumbers', str(phone))
    request.add_query_param('SignName', "leobod")
    request.add_query_param('TemplateCode', "SMS_175532958")
    dict = {"code": str(code)}
    json_dict = json.dumps(dict)
    request.add_query_param('TemplateParam', json_dict)
    return request

# 调用Client、request来调用SmsApi
def actionSendSms(phone, code):
    client = initClient()
    request = initSmsParameter(str(phone), str(code))
    response = client.do_action(request)                # class bytes
    res = str(response, encoding="utf-8")               # class str
    r = json.loads(res)                                 # class dict
    return r

    # if r["Code"] == "OK":
    #     return True
    # else:
    #     return False


'''
Type response <class 'bytes'>
{"Message":"OK","RequestId":"B07D47AE-06D6-4966-B011-168727C7A141","BizId":"402617584525830937^0","Code":"OK"}
Type res <class 'str'>
<class 'dict'>
'''

'''
{"Message":"139523483377invalid mobile number","RequestId":"84A18172-BA0D-4AAB-A9FA-C8F484C29AE3","Code":"isv.MOBILE_NUMBER_ILLEGAL"}
'''

'''
{"Message":"params must be [a-zA-Z0-9] for verification sms","RequestId":"F9E11FAE-799D-44B5-9425-2AF2CA1BD666","Code":"isv.INVALID_PARAMETERS"}
'''


if __name__ == "__main__":
    actionSendSms("13952348337", "中文类容")
