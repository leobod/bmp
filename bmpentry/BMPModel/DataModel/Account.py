"""
    @File: Account.py
    @Type: class -> (model)
    @Description: 与数据库进行关系映射的类 Account

    @Author: Leobod
    @Version: 1.0.0
    @Modify Time: 2020-02-19

    @Contract: leobod@eside.cn
    @License: ©2019-2020 leobod 苏ICP备17004905号
"""

from django.db import models
import json

class Account(models.Model):
    aid = models.AutoField(name="aid", max_length=10, primary_key=True, db_column="aid")
    phone = models.CharField(name="phone", max_length=11, unique=True, db_column="phone")
    salt = models.CharField(name="salt", max_length=10, unique=True, db_column="salt", default="md5")
    password = models.CharField(name="password", max_length=50, db_column="password")
    astatus = models.BooleanField(name="astatus", db_column="astatus")
    modify_time = models.DateTimeField(auto_now=True, db_column="modify_time")
    create_time = models.DateTimeField(auto_now_add=True, db_column="create_time")

    class Meta:
        db_table = "account"

    def __str__(self) -> dict:
        querydata = {
            "aid" : self.aid,
            "phone": self.phone,
            "salt": self.salt,
            "password": self.password,
            "astatus": self.astatus,
            "modify_time": self.modify_time,
            "create_time": self.create_time
        }
        return querydata

