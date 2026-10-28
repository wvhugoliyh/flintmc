from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from flintmc.nodes import Node

if TYPE_CHECKING:
    from flintmc.nodes import Value


@dataclass(slots=True)
class BinaryOp(Node):
    operand_1: Value
    operator: Literal[
        "+", "-", "*", "/", "^",
        "||", "&&",
        "==", "!=", "<=", ">=", "<", ">",
    ]
    operand_2: Value