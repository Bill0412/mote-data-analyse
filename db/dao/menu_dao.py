from typing import Dict, Any
from db.entity.menu_do import MenuDO
import datetime


def insert_menu(params: Dict[str, Any]) -> None:
    params['gmt_create'] = datetime.datetime.utcnow()
    params['gmt_modified'] = datetime.datetime.utcnow()
    MenuDO.create(**params)