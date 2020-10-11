from peewee import Model, MySQLDatabase

from config import mysql_config

try:
    db = MySQLDatabase(**mysql_config)
except Exception:
    print('[ERROR] db config not found')


class BaseDO(Model):
    class Meta:
        database = db
