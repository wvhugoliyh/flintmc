from dataclasses import dataclass
from typing import TYPE_CHECKING

from flintmc.nodes import Node

if TYPE_CHECKING:
    from flintmc.nodes import ResourceLocation, Value


@dataclass(slots=True)
class FuncCall(Node):
    function: ResourceLocation
    args: list[Value]