import datetime
from db.entity.outlet_do import OutletDO
from typing import Dict, Any, List
from playhouse.shortcuts import model_to_dict


def insert_outlet(params: Dict[str, Any]) -> None:
    params['gmt_create'] = datetime.datetime.utcnow()
    params['gmt_modified'] = datetime.datetime.utcnow()
    OutletDO.create(**params)


def get_outlet_by_id_outlet(id_outlet: str) -> OutletDO:
    return OutletDO.get(OutletDO.id_outlet == id_outlet)


def get_outlet_by_source(source: str) -> List[OutletDO]:
    return list(OutletDO.select().where(OutletDO.source == source).execute())


def get_outlet_by_source_dict(source: str) -> List[Dict[str, Any]]:
    """
    :param source: the source of the outlet, query parameter
    :return: converts the OutletDO's to dict's and returns a list of them
    """
    return [model_to_dict(outlet_do, recurse=True) for outlet_do in get_outlet_by_source(source)]
