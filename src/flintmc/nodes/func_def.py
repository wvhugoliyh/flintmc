from dataclasses import dataclass
from typing import TYPE_CHECKING

from flintmc.nodes import Node

if TYPE_CHECKING:
    from flintmc.nodes import ResourceLocation, Statement


@dataclass(slots=True)
class FuncDef(Node):
    function: ResourceLocation
    params: list[str]
    statements: list[Statement]