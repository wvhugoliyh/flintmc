from dataclasses import dataclass

from flintmc.nodes.expression import ResourceLocation

from flintmc.nodes.statements import stmtT

type definitionT = FuncDef | TickDef | LoadDef

@dataclass
class FuncDef:
  resource_loc: ResourceLocation
  params: list[str]
  stmts: list[stmtT]

@dataclass
class TickDef:
  resource_loc: ResourceLocation
  stmts: list[stmtT]

@dataclass
class LoadDef:
  resource_loc: ResourceLocation
  stmts: list[stmtT]