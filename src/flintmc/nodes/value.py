from typing import TypeAlias

from flintmc.nodes.array_item import ArrayItem
from flintmc.nodes.binary_op import BinaryOp
from flintmc.nodes.func_call import FuncCall
from flintmc.nodes.property import Property
from flintmc.nodes.unary_op import UnaryOp

Value: TypeAlias = (
    ArrayItem | BinaryOp | FuncCall | Property | UnaryOp |
    bool | dict | float | int | list | str
)