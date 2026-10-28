from dataclasses import dataclass
from typing import TYPE_CHECKING

from flintmc.nodes.node import Node

if TYPE_CHECKING:
    from flintmc.nodes import NBTLocation

@dataclass(slots=True)
class Variable(Node):
    nbt_loc: NBTLocation
    id: str