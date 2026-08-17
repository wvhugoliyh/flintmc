from dataclasses import dataclass

from flintmc.nodes.expression import boolean_value
from flintmc.nodes.statements import stmt

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