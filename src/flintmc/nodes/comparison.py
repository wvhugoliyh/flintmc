from dataclasses import dataclass
from typing import TYPE_CHECKING

from flintmc.nodes.node import Node

if TYPE_CHECKING:
    from flintmc.nodes import Comparator, Value


@dataclass(slots=True)
class Comparison(Node):
    comparand_1: Value
    comparator: Comparator
    comparand_2: Value