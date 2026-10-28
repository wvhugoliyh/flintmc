from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from flintmc.nodes import (
        ArrayItem,
        FuncCall,
        LogicBinaryOp,
        MathBinaryOp,
        Negation,
        Negative,
        Property,
        Variable,
    )

type Value = (
    ArrayItem
    | FuncCall
    | LogicBinaryOp
    | MathBinaryOp
    | Negation
    | Negative
    | Property
    | Variable
    | bool
    | dict
    | float
    | int
    | list
    | str
)