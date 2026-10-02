from dataclasses import dataclass
from typing import Literal

from flintmc.nodes import NodeType

type numeric_value = (MathBinaryOp | int | float
                   | tuple[ResourceLocation, str])

type boolean_value = LogicBinaryOp | Comparison | bool


@dataclass(repr=True)
class MathBinaryOp(NodeType):
  opnd_1: numeric_value
  opr: Literal["+", "-", "*", "/", "^"]
  opnd_2: numeric_value

@dataclass(repr=True)
class MathNeg(NodeType):
  opnd: numeric_value

@dataclass(repr=True)
class LogicBinaryOp(NodeType):
  opnd_1: boolean_value
  opr: Literal["||", "&&"]
  opnd_2: boolean_value

@dataclass(repr=True)
class LogicNot(NodeType):
  opnd: boolean_value

@dataclass(repr=True)
class Comparison(NodeType):
  cmpnd_1: numeric_value
  cmpr: Literal["==", "!=", "<", ">", "<=", ">="]
  cmpnd_2: numeric_value

@dataclass(repr=True)
class EntityProp:
  entity_sel: str
  nbt_path_comps: list[str]

  def __repr__(self):
    return f"{self.entity_sel}.{".".join(self.nbt_path_comps)}"

@dataclass(repr=True)
class ResourceLocation:
  namespace: str
  id: str

  def __repr__(self):
    return f"{self.namespace}:{self.id}"