from dataclasses import dataclass
from typing import TYPE_CHECKING

from flintmc.nodes import Node

if TYPE_CHECKING:
    from flintmc.nodes import Value


@dataclass(slots=True)
class ArrayItem(Node):
    array: Value
    index: Value