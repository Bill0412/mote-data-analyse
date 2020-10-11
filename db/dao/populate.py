from db.entity.menu_do import MenuDO
from db.entity.review_do import ReviewDO
from db.entity.user_do import UserDO
from db.entity.outlet_do import OutletDO
from peewee import MySQLDatabase
from typing import Dict


MODELS = [OutletDO, UserDO, ReviewDO, MenuDO]


def populate_db(mysql_config: Dict[str, str], drop_exist: bool = False) -> None:
    db = MySQLDatabase(**mysql_config)
    db.bind(MODELS, bind_refs=False, bind_backrefs=False)
    db.connect()
    if drop_exist:
        db.drop_tables(MODELS)
    db.create_tables(MODELS)
