from dataclasses import dataclass
from typing import Literal

from flintmc.nodes import Node


@dataclass(slots=True)
class TargetSelector(Node):
    selector_var: Literal["n", "p", "s", "r"]