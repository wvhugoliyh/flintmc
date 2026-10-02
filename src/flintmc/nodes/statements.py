from dataclasses import dataclass
from typing import Any, TYPE_CHECKING

from flintmc.nodes import NodeType

if TYPE_CHECKING:
  from flintmc.nodes import (
    ResourceLocation,
    numeric_value,
    boolean_value,
  )

# Type aliases are used to reduce repetitive code
type stmtT = Assignment | FuncCall | Conditional | Repeat | Execute | Run


@dataclass
class Assignment(NodeType):
  id: tuple(ResourceLocation, str)
  value: numeric_value

@dataclass
class FuncCall(NodeType):
  resource_loc: ResourceLocation
  args: list[numeric_value]

@dataclass
class Conditional(NodeType):
  if_stmt: If
  elif_stmts: list[Elif]
  else_stmt: Else | None

@dataclass
class Repeat(NodeType):
  repeat_cnt: int
  stmts: list[stmtT]

@dataclass
class Execute(NodeType):
  exec_args: list[ExecArg]
  stmts: list[stmtT]

@dataclass
class Run:
  raw: str

  def __repr__(self):
    return self.raw


@dataclass
class If(NodeType):
  condition: boolean_value
  stmts: list[stmtT]

@dataclass
class Elif(NodeType):
  condition: boolean_value
  stmts: list[stmtT]

@dataclass
class Else(NodeType):
  stmts: list[stmtT]

@dataclass
class ExecArg:
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

  def __repr__(self):
    return f"{self.cmd} {" ".join(self.args)}"