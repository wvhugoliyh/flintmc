from typing import TypeAlias

from flintmc.nodes import ArrayItem, BinaryOp, FuncCall, Property

Value: TypeAlias = (
    ArrayItem | BinaryOp | FuncCall | Property |
    bool | dict | float | int | list | str
)