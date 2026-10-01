from dataclasses import dataclass

from flintmc.nodes import (
  NodeType,
  ResourceLocation,
  stmtT,
)

type definitionT = FuncDef | TickDef | LoadDef

@dataclass
class FuncDef(NodeType):
  resource_loc: ResourceLocation
  params: list[str]
  stmts: list[stmtT]

@dataclass
class TickDef(NodeType):
  resource_loc: ResourceLocation
  stmts: list[stmtT]

@dataclass
class LoadDef(NodeType):
  resource_loc: ResourceLocation
  stmts: list[stmtT]