""""""
from typing import TypeAliasType

def filter_by_type(objs: list, type: type | TypeAliasType):
  """ Filters a list by type. Supports filter by type alias.

  Instance of a subclass is considered instance of the base class.
  """

  try:
    return list(filter(type.__instancecheck__, objs))

  except AttributeError:
    return list(filter(lambda obj: isinstance(type.__value__, obj), objs))