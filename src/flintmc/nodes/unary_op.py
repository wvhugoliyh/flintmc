from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from flintmc.nodes import Node

if TYPE_CHECKING:
    from flintmc.nodes import Value


@dataclass(slots=True)
class UnaryOp(Node):
    operator: Literal["-", "!"]
    operand: Value