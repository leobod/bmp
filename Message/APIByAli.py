#!/usr/bin/env python
#coding=utf-8

import json
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest

from Message.APICONST import ALIYUN_SETTINGS, ALIYUN_SMS_ACTION

def initClient():
    client = AcsClient(
        ALIYUN_SETTINGS["access"]["accessKeyId"],
        ALIYUN_SETTINGS["access"]["accessSecret"],
        ALIYUN_SETTINGS["access"]["RegionId"]
    )
    return client

def initSmsHeader():
    request = CommonRequest()
    request.set_accept_format(ALIYUN_SETTINGS["sms"]["accept_format"])
    request.set_domain(ALIYUN_SETTINGS["sms"]["domain"])
    request.set_method(ALIYUN_SETTINGS["sms"]["method"])
    request.set_protocol_type(ALIYUN_SETTINGS["sms"]["protocol_type"]) # https | http
    request.set_version(ALIYUN_SETTINGS["sms"]["version"])
    return request

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

def actionSendSms(phone, code):
    client = initClient()
    request = initSmsParameter(str(phone), str(code))
    response = client.do_action(request)
    print("Type response %s" %(type(response)))
    res = str(response, encoding="utf-8")
    print(res)
    print("Type res %s" %(type(res)))
    r = json.loads(res)
    print(type(r))

'''
Type response <class 'bytes'>
{"Message":"OK","RequestId":"B07D47AE-06D6-4966-B011-168727C7A141","BizId":"402617584525830937^0","Code":"OK"}
Type res <class 'str'>
<class 'dict'>
'''


if __name__ == "__main__":
    actionSendSms("13952348337", "lovejiangjiang")


