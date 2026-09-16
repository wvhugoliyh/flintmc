from dataclasses import dataclass

from flintmc.nodes.statements import stmtT

type definitionT = FuncDef | TickDef | LoadDef

@dataclass
class FuncDef:
  id: str
  params: list[str]
  stmts: list[stmtT]

@dataclass
class TickDef:
  id: str
  stmts: list[stmtT]

@dataclass
class LoadDef:
  id: str
  stmts: list[stmtT]