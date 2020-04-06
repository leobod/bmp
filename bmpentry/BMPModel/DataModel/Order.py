"""
    @File: Order.py
    @Type: class -> (model)
    @Description: 与数据库进行关系映射的类 Order

    @Author: Leobod
    @Version: 1.0.0
    @Modify Time: 2020-02-19

    @Contract: leobod@eside.cn
    @License: ©2019-2020 leobod 苏ICP备17004905号
"""
from datetime import datetime

from django.db import models
import json

from .Account import Account

class Order(models.Model):
    oid = models.AutoField(name="oid", max_length=10, primary_key=True, db_column="oid")
    aid = models.ForeignKey(Account, models.CASCADE, db_column="aid")
    ostatus = models.IntegerField(name="ostatus", max_length="1", db_column="ostatus")
    oratiored = models.FloatField(name="oratiored", db_column="oratiored", blank=True)
    oratiogreen = models.FloatField(name="oratiogreen", db_column="oratiogreen", blank=True)
    oratioother = models.FloatField(name="oratioother", db_column="oratioother", blank=True)
    oresulta = models.IntegerField(name="oresulta", max_length="1", db_column="oresulta")
    oresultb = models.IntegerField(name="oresultb", max_length="1", db_column="oresultb")
    oresultall = models.IntegerField(name="oresultall", max_length="1", db_column="oresultall")
    odir = models.CharField(name="odir", max_length=30, db_column="odir")

    class Meta:
        db_table = "order"

    def __str__(self):
        pass


