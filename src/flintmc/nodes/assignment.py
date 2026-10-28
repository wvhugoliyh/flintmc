from dataclasses import dataclass
from typing import TYPE_CHECKING

from flintmc.nodes import Node

if TYPE_CHECKING:
    from flintmc.nodes import Value, Variable


@dataclass(slots=True)
class Assignment(Node):
    variable: Variable
    value: Value