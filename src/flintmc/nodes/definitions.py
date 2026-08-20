from dataclasses import dataclass

from flintmc.nodes.statements import stmt


@dataclass
class FuncDef:
  func_id: str
  params: list[str]
  stmts: list[stmt]

@dataclass
class TickDef:
  tick_id: str
  stmts: list[stmt]

@dataclass
class LoadDef:
  load_id: str
  stmts: list[stmt]