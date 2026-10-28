from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from flintmc.nodes import Node

if TYPE_CHECKING:
    from flintmc.nodes import Comparator, Value


@dataclass(slots=True)
class BinaryOp(Node):
    operand_1: Value
    operator: Literal["+", "-", "*", "/", "^", "||", "&&"] | Comparator
    operand_2: Value