from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from flintmc.nodes import ArrayItem, Property, Variable

type Assignable = ArrayItem | Property | Variable