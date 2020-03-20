# 中间量表的对应的model类

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

