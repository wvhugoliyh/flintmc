from typing import TypeAlias

from flintmc.nodes import Assignment, FuncCall, Raw

Statement: TypeAlias = Assignment | FuncCall | Raw