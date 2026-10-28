from typing import TypeAlias

from flintmc.nodes import ArrayItem, BinaryOp, FuncCall, Property, UnaryOp

Value: TypeAlias = (
    ArrayItem | BinaryOp | FuncCall | Property | UnaryOp |
    bool | dict | float | int | list | str
)