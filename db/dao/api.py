from db.entity.outlet_do import OutletDO
from db.entity.menu_do import MenuDO
from typing import Dict, Any, List
from playhouse.shortcuts import model_to_dict


def get_outlet_contains_brand(brand: str) -> List[OutletDO]:
    return list(set(OutletDO.select().join(MenuDO).where(MenuDO.brand.contains(brand)).execute()))


def get_outlet_contains_brand_dict(brand: str) -> List[Dict[str, Any]]:
    return [model_to_dict(outlet_do, recurse=True) for outlet_do in get_outlet_contains_brand(brand)]