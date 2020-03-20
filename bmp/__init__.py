
# pymysql依赖配置
# 使用自定义版本号，解决兼容性问题
import pymysql
pymysql.version_info = (1, 3, 13, "final", 0)
pymysql.install_as_MySQLdb()