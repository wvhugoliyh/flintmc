from dataclasses import dataclass
from typing import TYPE_CHECKING

from flintmc.nodes.node import Node

if TYPE_CHECKING:
    from flintmc.nodes import Assignable, Value


@dataclass(slots=True)
class Assignment(Node):
    variable: Assignable
    value: Value