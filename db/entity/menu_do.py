from .base_do import BaseDO
from .outlet_do import OutletDO

from peewee import BigAutoField, ForeignKeyField, CharField, DoubleField, IntegerField, DateTimeField


class MenuDO(BaseDO):
    class Meta:
        table_name = 'menu'

    id = BigAutoField()
    outlet_id = ForeignKeyField(OutletDO)
    brand = CharField()
    price = DoubleField()
    volume = IntegerField()
    name = CharField()
    gmt_create = DateTimeField()
    gmt_modified = DateTimeField()
