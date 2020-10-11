from typing import Dict, Any, List
from db.entity.menu_do import MenuDO
from playhouse.shortcuts import model_to_dict
import datetime


def insert_menu(params: Dict[str, Any]) -> None:
    params['gmt_create'] = datetime.datetime.utcnow()
    params['gmt_modified'] = datetime.datetime.utcnow()
    MenuDO.create(**params)


def get_menu_above_price(price: float) -> List[MenuDO]:
    return list(MenuDO.select().where(MenuDO.price > price).execute())


def get_menu_above_price_dict(price: float) -> List[Dict[str, Any]]:
    """
    :param price: the price threshold
    :return: a list of dicts with all the menu items with price above the threshold
    """
    return [model_to_dict(menu_do, recurse=False) for menu_do in get_menu_above_price(price)]
