from dataclasses import dataclass
from typing import TYPE_CHECKING

from flintmc.nodes.node import Node

if TYPE_CHECKING:
    from flintmc.nodes import ResourceLocation, Value


@dataclass(slots=True)
class FuncCall(Node):
    rsrc_loc: ResourceLocation
    args: list[Value]