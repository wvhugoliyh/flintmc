from typing import TypeAlias

from flintmc.nodes.array_item import ArrayItem
from flintmc.nodes.func_call import FuncCall
from flintmc.nodes.logic_binary_op import LogicBinaryOp
from flintmc.nodes.math_binary_op import MathBinaryOp
from flintmc.nodes.negation import Negation
from flintmc.nodes.negative import Negative
from flintmc.nodes.property import Property

Value: TypeAlias = (
    ArrayItem
    | FuncCall
    | LogicBinaryOp
    | MathBinaryOp
    | Negation
    | Negative
    | Property
    | bool
    | dict
    | float
    | int
    | list
    | str
)