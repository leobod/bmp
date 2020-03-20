
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