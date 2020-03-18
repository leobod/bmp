# 阿里云API

## 短信API

### SendSms

调用SendSms发送短信。

SendSms接口是短信发送接口，支持在一次请求中向多个不同的手机号码发送同样内容的短信。

如果您需要在一次请求中分别向多个不同的手机号码发送不同签名和模版内容的短信，请使用SendBatchSms接口。

#### Required Parameter

```
RegionId            地区ID
PhoneNumbers        接收短信的手机号码
SignName            短信签名名称。请在签名管理页面签名名称一列查看
TemplateCode        短信模板ID。请在模板管理页面模板CODE一列查看,要求传入JSON
```

#### Optional Parameter

```
TemplateParam				短信模板变量对应的实际值，JSON格式。
SmsUpExtendCode			上行短信扩展码，无特殊需要此字段的用户请忽略此字段。
OutId							外部流水扩展字段。
```



### QuerySendDetails

调用QuerySendDetails接口查看短信发送记录和发送状态。

通过调用QuerySendDetails接口，可以根据短信发送日期查看发送记录和短信内容，也可以添加发送流水号，根据流水号查询指定日期指定请求的发送详情。

如果指定日期短信发送量较大，可以分页查看。指定每页显示的短信详情数量和查看的页数，即可分页查看发送记录。

#### Required Parameter

```
PhoneNumber					接收短信的手机号码。
SendDate						短信发送日期，支持查询最近30天的记录。格式为yyyyMMdd
PageSize						分页查看发送记录，指定每页显示的短信记录数量。取值范围为1~50。
CurrentPage					分页查看发送记录，指定发送记录的的当前页码。
```

#### Optional Parameter

```
BizId								发送回执ID，即发送流水号
```

