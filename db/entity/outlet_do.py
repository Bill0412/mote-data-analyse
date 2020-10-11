from .base_do import BaseDO
from peewee import BigAutoField, CharField, IntegerField, DateTimeField


class OutletDO(BaseDO):
    class Meta:
        table_name = 'outlet'

    id = BigAutoField()
    id_outlet = CharField(index=True, unique=True)
    name = CharField()
    source = CharField()
    address = CharField()
    country = CharField(max_length=2)
    phone = CharField()
    reviews_nr = IntegerField()
    gmt_create = DateTimeField()
    gmt_modified = DateTimeField()
