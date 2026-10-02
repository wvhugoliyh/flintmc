from dataclasses import dataclass
from typing import TYPE_CHECKING

from flintmc.nodes import NodeType

if TYPE_CHECKING:
  from flintmc.nodes import (
    ResourceLocation,
    stmtT,
  )

type definitionT = FuncDef | TickDef | LoadDef

@dataclass(repr=False)
class FuncDef(NodeType):
  resource_loc: ResourceLocation
  params: list[str]
  stmts: list[stmtT]

@dataclass(repr=False)
class TickDef(NodeType):
  resource_loc: ResourceLocation
  stmts: list[stmtT]

@dataclass(repr=False)
class LoadDef(NodeType):
  resource_loc: ResourceLocation
  stmts: list[stmtT]