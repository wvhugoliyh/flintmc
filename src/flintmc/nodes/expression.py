from dataclasses import dataclass
from typing import Literal

# Type aliases are used to reduce repetitive code
type numeric_value = (MathBinaryOp | int | float
                   | tuple[ResourceLocation, str])

type boolean_value = LogicBinaryOp | Comparison | bool


@dataclass
class MathBinaryOp:
  opnd_1: numeric_value
  opr: Literal["+", "-", "*", "/", "^"]
  opnd_2: numeric_value

@dataclass
class MathNeg:
  opnd: numeric_value

@dataclass
class LogicBinaryOp:
  opnd_1: boolean_value
  opr: Literal["||", "&&"]
  opnd_2: boolean_value

@dataclass
class LogicNot:
  opnd: boolean_value

@dataclass
class Comparison:
  cmpnd_1: numeric_value
  cmpr: Literal["==", "!=", "<", ">", "<=", ">="]
  cmpnd_2: numeric_value

@dataclass
class EntityProp:
  entity_sel: str
  nbt_path_comps: list[str]

@dataclass
class ResourceLocation:
  namespace: str
  id: str

  def __repr__(self):
    return f"{self.namespace}:{self.id}"