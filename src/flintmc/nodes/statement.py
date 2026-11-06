from typing import TypeAlias

from flintmc.nodes.assignment import Assignment
from flintmc.nodes.func_call import FuncCall
from flintmc.nodes.raw import Raw

Statement: TypeAlias = Assignment | FuncCall | Raw