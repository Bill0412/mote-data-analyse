from peewee import Model, Proxy

db_proxy = Proxy()

class BaseDO(Model):
    class Meta:
        database = db_proxy
