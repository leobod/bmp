"""
    @File: User.py
    @Type: class -> (model)
    @Description: 与数据库进行关系映射的类 User

    @Author: Leobod
    @Version: 1.0.0
    @Modify Time: 2020-02-19

    @Contract: leobod@eside.cn
    @License: ©2019-2020 leobod 苏ICP备17004905号
"""

from django.db import models
from .Account import Account

class User(models.Model):
    uid = models.AutoField(name="uid", max_length=10, primary_key=True, db_column="uid")
    aid = models.OneToOneField(Account, models.CASCADE, db_column="aid")
    uname = models.CharField(name="uname", max_length=15, db_column="uname")
    ugender = models.CharField(name="ugender", max_length=2, db_column="ugender", blank=True)
    uemail = models.CharField(name="uemail", max_length=30, db_column="uemail", blank=True)

    class Meta:
        db_table = "user"

    def __str__(self):
        querydata = {
            "uid": self.uid,
            "aid": self.aid,
            "uname": self.uname,
            "ugender": self.ugender,
            "uemail": self.uemail
        }
        return querydata

