from .base_do import BaseDO
from .user_do import UserDO
from .outlet_do import OutletDO

from peewee import BigAutoField, ForeignKeyField, DateField, CharField, DoubleField, DateTimeField


class ReviewDO(BaseDO):
    class Meta:
        table_name = 'review'

    id = BigAutoField()
    user = ForeignKeyField(UserDO)
    outlet = ForeignKeyField(OutletDO)
    date = DateField()
    review = CharField()
    rating = DoubleField()
    gmt_create = DateTimeField()
    gmt_modified = DateTimeField()
