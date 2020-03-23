"""
    @File: Middle.py
    @Type: class -> (model)
    @Description: 与数据库进行关系映射的类 Middle

    @Author: Leobod
    @Version: 1.0.0
    @Modify Time: 2020-02-19

    @Contract: leobod@eside.cn
    @License: ©2019-2020 leobod 苏ICP备17004905号
"""

from django.db import models
import json
from .Order import Order

class Middle(models.Model):
    mid = models.AutoField(name="mid", max_length=10, primary_key=True, db_column="mid")
    oid = models.ForeignKey(Order, models.CASCADE, db_column="oid")
    mtype = models.IntegerField(name="mtype", max_length=6, db_column="mtype")
    mpath = models.CharField(name="mpath", max_length=30, db_column="mpath")

    class Meta:
        db_table = "middle"

    def __str__(self):
        querydata = {
            "mid": self.mid,
            "oid": self.oid,
            "mtype": self.mtype,
            "mpath": self.mpath,
        }
        return querydata

