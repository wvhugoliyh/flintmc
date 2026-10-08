from dataclasses import dataclass
from typing import Literal

from flintmc.nodes import NodeType

type numeric_value = MathBinaryOp | int | float | Variable

type boolean_value = LogicBinaryOp | Comparison | bool


@dataclass(repr=False)
class MathBinaryOp(NodeType):
  opnd_1: numeric_value
  opr: Literal["+", "-", "*", "/", "^"]
  opnd_2: numeric_value

@dataclass(repr=False)
class MathNeg(NodeType):
  opnd: numeric_value

@dataclass(repr=False)
class LogicBinaryOp(NodeType):
  opnd_1: boolean_value
  opr: Literal["||", "&&"]
  opnd_2: boolean_value

@dataclass(repr=False)
class LogicNot(NodeType):
  opnd: boolean_value

@dataclass(repr=False)
class Comparison(NodeType):
  cmpnd_1: numeric_value
  cmpr: Literal["==", "!=", "<", ">", "<=", ">="]
  cmpnd_2: numeric_value

@dataclass(repr=False)
class EntityProp(NodeType):
  entity_sel: str
  nbt_path_comps: list[str]

@dataclass(repr=False)
class ResourceLocation(NodeType):
  namespace: str
  id: str

  def __repr__(self):
    return f"{self.namespace}:{self.id}"

@dataclass(repr=False)
class Variable(NodeType):
  resource_loc: ResourceLocation
  id: str

@dataclass(repr=False)
class Raw(NodeType):
  raw: str

  def __repr__(self):
    return raw