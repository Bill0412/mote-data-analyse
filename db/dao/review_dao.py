from db.entity.review_do import ReviewDO
from typing import Dict, Any
import datetime


def insert_review(params: Dict[str, Any]) -> None:
    params['gmt_create'] = datetime.datetime.utcnow()
    params['gmt_modified'] = datetime.datetime.utcnow()
    ReviewDO.create(**params)
