"""
    @File: AliConst.py
    @Type: const -> (custom)
    @Description: 记录阿里巴巴的接口的配置常量

    @Author: Leobod
    @Version: 1.0.0
    @Modify Time: 2020-02-18

    @Contract: leobod@eside.cn
    @License: ©2019-2020 leobod 苏ICP备17004905号
"""

# # Code Start
ALIYUN_SETTINGS = {
    "access": {
        "accessKeyId": "LTAI4FejSAgkHvV9MSqFJizW",
        "accessSecret": "LdMqXps0voHwq61JvZv9aJm4h2yFpO",
        "RegionId": "cn-hangzhou"
    },
    "sms": {
        "accept_format": "json",
        "domain": "dysmsapi.aliyuncs.com",
        "method": "POST",
        "protocol_type": "https",
        "version": "2017-05-25",
    },
}


ALIYUN_SMS_ACTION = {
        "sendsms":{
            "name": "SendSms",
            "required": ["RegionId", "PhoneNumbers", "SignName", "TemplateCode",],
            "optional": ["TemplateParam", "SmsUpExtendCode", "OutId"]
        }
}