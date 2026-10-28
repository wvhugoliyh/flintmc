from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from flintmc.nodes import Assignment, FuncCall, Raw

type Statement = Assignment | FuncCall | Raw