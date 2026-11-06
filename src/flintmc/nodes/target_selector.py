from dataclasses import dataclass
from typing import Literal

from flintmc.nodes.node import Node


@dataclass(slots=True)
class TargetSelector(Node):
    variable: Literal["n", "p", "s", "r"]