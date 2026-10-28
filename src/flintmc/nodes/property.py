from dataclasses import dataclass
from typing import TYPE_CHECKING

from flintmc.nodes import Node

if TYPE_CHECKING:
    from flintmc.nodes import NBTLocation, Value


@dataclass(slots=True)
class Property(Node):
    map: NBTLocation | Value
    property_id: str