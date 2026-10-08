from dataclasses import dataclass
from typing import Any, TYPE_CHECKING

from flintmc.nodes import NodeType

if TYPE_CHECKING:
  from flintmc.nodes import (
    Raw,
    ResourceLocation,
    Variable,
    numeric_value,
    boolean_value,
  )

# Type aliases are used to reduce repetitive code
type stmtT = Assignment | FuncCall | Conditional | Repeat | Execute | Run


@dataclass(repr=False)
class Assignment(NodeType):
  var: Variable
  value: numeric_value

@dataclass(repr=False)
class FuncCall(NodeType):
  resource_loc: ResourceLocation
  args: list[numeric_value]

@dataclass(repr=False)
class Conditional(NodeType):
  if_stmt: If
  else_stmt: Else | None

@dataclass(repr=False)
class Repeat(NodeType):
  repeat_cnt: int
  stmts: list[stmtT]

@dataclass(repr=False)
class Execute(NodeType):
  raw: Raw
  stmts: list[stmtT]

@dataclass(repr=False)
class Run(NodeType):
  raw: Raw

@dataclass(repr=False)
class If(NodeType):
  condition: boolean_value
  stmts: list[stmtT]

@dataclass(repr=False)
class Else(NodeType):
  stmts: list[stmtT]