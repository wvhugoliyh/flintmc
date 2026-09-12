from dataclasses import dataclass
from typing import Any

from flintmc.nodes.expression import numeric_value, boolean_value

# Type aliases are used to reduce repetitive code
type stmt = Assignment | FuncCall | Conditional | Repeat | Execute


@dataclass
class Assignment:
  var_id: str
  value: numeric_value

@dataclass
class FuncCall:
  func_id: str
  args: list[numeric_value]

@dataclass
class Conditional:
  if_stmt: If
  elif_stmts: list[Elif]
  else_stmt: Else | Literal[None]

@dataclass
class Repeat:
  repeat_cnt: int
  stmts: list[stmt]

@dataclass
class Execute:
  exec_args: list[ExecArg]
  stmts: list[stmt]

@dataclass
class Run:
  raw: str


@dataclass
class If:
  condition: boolean_value
  stmts: list[stmt]

@dataclass
class Elif:
  condition: boolean_value
  stmts: list[stmt]

@dataclass
class Else:
  stmts: list[stmt]

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