# 系统介绍与配置使用说明

## 系统介绍
暂无介绍

## BMPConst文件说明

### BMPConst包含系统的配置信息
不对外公开，请谅解，写这部分的原因就是，如果开源时候拿到了code，请自行补上

### 文件1-AliConst.py
形式如同
```python 
## 文件路径： $project/bmpentry/BMPConst/AliConst.py
## Code Start
ALIYUN_SETTINGS = {
    "access": {
        "accessKeyId": "...........",
        "accessSecret": "................",
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
```

### 文件2-DataBaseConst.py
形式如同
```python 
## 文件路径： $project/bmpentry/BMPConst/DataBaseConst.py
## Code Start
DataBase_BMP = {
    "engine": "django.db.backends.mysql",
    "name": ".......",
    "user": ".........",
    "password": ".............",
    "host": ".....................",
    "port": "3306"
}
```

## 数据库的配置
请使用bmp-DataStructure.sql文件自行构建