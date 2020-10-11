from db.entity.user_do import UserDO
from typing import Dict, Any
import datetime


def insert_user(params: Dict[str, Any]) -> None:
    params['gmt_create'] = datetime.datetime.utcnow()
    params['gmt_modified'] = datetime.datetime.utcnow()
    UserDO.create(**params)


def get_user_by_name(name: str) -> UserDO:
    return UserDO.get(UserDO.user == name)
