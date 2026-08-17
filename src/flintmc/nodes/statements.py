from dataclasses import dataclass

from flintmc.nodes.expression import numeric_value
from flintmc.nodes.conditional import If, Elif, Else

# Type aliases are used to reduce repetitive code
type stmt = Assignment | FuncCall | Conditional | Repeat


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