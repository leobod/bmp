"""
    @File: Smscode.py
    @Type: class -> (model)
    @Description: 与数据库进行关系映射的类 Smscode

    @Author: Leobod
    @Version: 1.0.0
    @Modify Time: 2020-02-19

    @Contract: leobod@eside.cn
    @License: ©2019-2020 leobod 苏ICP备17004905号
"""

from django.db import models
import json

class Smscode(models.Model):
    sid = models.AutoField(name="sid", max_length=10, primary_key=True, db_column="sid")
    phone = models.CharField(name="phone", max_length=11, db_column="phone")
    code = models.CharField(name="code", max_length=6, db_column="code")
    bizcode = models.CharField(name="bizcode", max_length=20, db_column="bizcode")
    effective_time = models.DateTimeField(auto_now=True, db_column="effective_time")        # 解决时间问题
    create_time = models.DateTimeField(auto_now_add=True, db_column="create_time")

    class Meta:
        db_table = "smscode"

    def __str__(self):
        querydata = {
            "sid" : self.sid,
            "phone": self.phone,
            "code": self.code,
            "bizcode": self.bizcode,
            "effective_time": self.effective_time,
            "create_time": self.create_time
        }
        return querydata

