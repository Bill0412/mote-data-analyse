import datetime
from db.entity.outlet_do import OutletDO
from typing import Dict, Any


def insert_outlet(params: Dict[str, Any]) -> None:
    params['gmt_create'] = datetime.datetime.utcnow()
    params['gmt_modified'] = datetime.datetime.utcnow()
    OutletDO.create(**params)


def get_outlet_by_id_outlet(id_outlet: str) -> OutletDO:
    return OutletDO.get(OutletDO.id_outlet == id_outlet)
