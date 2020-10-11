from .base_do import BaseDO

from peewee import Model, BigAutoField, CharField, FloatField, IntegerField, DateTimeField


class UserDO(BaseDO):
    class Meta:
        table_name = 'user'

    id = BigAutoField()
    user = CharField()
    source = CharField()
    likes = FloatField()
    reviews = IntegerField()
    gmt_create = DateTimeField()
    gmt_modified = DateTimeField()
