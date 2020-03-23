"""
    @File: Md5.py
    @Type: class -> (custom)
    @Description: 标注Md5加密方法

    @Author: Leobod
    @Version: 1.0.0
    @Modify Time: 2020-02-19

    @Contract: leobod@eside.cn
    @License: ©2019-2020 leobod 苏ICP备17004905号
"""


# # Code Start
import hashlib

class Md5:

    @staticmethod
    def getMd5(a1:str) -> str:
        # 创建md5对象
        hl = hashlib.md5()

        # Tips
        # 此处必须声明encode
        # 若写法为hl.update(str)  报错为： Unicode-objects must be encoded before hashing
        hl.update(a1.encode(encoding='utf-8'))

        return hl.hexdigest()
