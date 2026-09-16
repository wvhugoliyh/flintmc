from dataclasses import dataclass

from flintmc.nodes.statements import stmtT

type definitionT = FuncDef | TickDef | LoadDef

@dataclass
class FuncDef:
  func_id: str
  params: list[str]
  stmts: list[stmtT]

@dataclass
class TickDef:
  tick_id: str
  stmts: list[stmtT]

@dataclass
class LoadDef:
  load_id: str
  stmts: list[stmtT]