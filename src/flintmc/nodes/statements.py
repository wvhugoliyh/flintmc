from dataclasses import dataclass
from typing import Any

from flintmc.nodes.expression import numeric_value, boolean_value

# Type aliases are used to reduce repetitive code
type stmtT = Assignment | FuncCall | Conditional | Repeat | Execute | Run


@dataclass
class Assignment:
  id: str
  value: numeric_value

@dataclass
class FuncCall:
  id: str
  args: list[numeric_value]

@dataclass
class Conditional:
  if_stmt: If
  elif_stmts: list[Elif]
  else_stmt: Else | Literal[None]

@dataclass
class Repeat:
  repeat_cnt: int
  stmts: list[stmtT]

@dataclass
class Execute:
  exec_args: list[ExecArg]
  stmts: list[stmtT]

@dataclass
class Run:
  raw: str


@dataclass
class If:
  condition: boolean_value
  stmts: list[stmtT]

@dataclass
class Elif:
  condition: boolean_value
  stmts: list[stmtT]

@dataclass
class Else:
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