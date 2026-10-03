from dataclasses import dataclass
from typing import Any, TYPE_CHECKING

from flintmc.nodes import NodeType

if TYPE_CHECKING:
  from flintmc.nodes import (
    ResourceLocation,
    Variable,
    numeric_value,
    boolean_value,
  )

# Type aliases are used to reduce repetitive code
type stmtT = Assignment | FuncCall | Conditional | Repeat | Execute | Run


@dataclass(repr=False)
class Assignment(NodeType):
  id: tuple(ResourceLocation, str)
  value: numeric_value

@dataclass(repr=False)
class FuncCall(NodeType):
  resource_loc: ResourceLocation
  args: list[numeric_value]

@dataclass(repr=False)
class Conditional(NodeType):
  if_stmt: If
  elif_stmts: list[Elif]
  else_stmt: Else | None

@dataclass(repr=False)
class Repeat(NodeType):
  repeat_cnt: int
  stmts: list[stmtT]

@dataclass(repr=False)
class Execute(NodeType):
  exec_args: list[ExecArg]
  stmts: list[stmtT]

@dataclass(repr=False)
class Run(NodeType):
  raw: str

@dataclass(repr=False)
class If(NodeType):
  condition: boolean_value
  stmts: list[stmtT]

@dataclass(repr=False)
class Elif(NodeType):
  condition: boolean_value
  stmts: list[stmtT]

@dataclass(repr=False)
class Else(NodeType):
  stmts: list[stmtT]

@dataclass(repr=False)
class ExecArg(NodeType):
  cmd: Literal[
    "align",
    "anchored",
    "as",
    "at",
    "facing",
    "facing_entity",
    "in",
    "on",
    "pos",
    "pos_as",
    "pos_over",
    "rotated",
    "rotated_as",
    "summon",
  ]

  args: list[Any]