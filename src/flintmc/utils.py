from typing import TypeAliasType

def filter_by_type(objs: list, type: type) -> list:
  """ Filters a list by type. """

  return [obj for obj in objs if isinstance(obj, type)]