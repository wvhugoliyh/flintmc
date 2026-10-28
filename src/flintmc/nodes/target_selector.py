from dataclasses import dataclass
from typing import Any, Literal

from flintmc.nodes import Node


@dataclass(slots=True)
class TargetSelector(Node):
    variable: Literal["a", "e", "n", "p", "s", "r"]
    arguments: dict[Literal[
        "x", "y", "z",
        "distance",
        "dx", "dy", "dz",
        "x_rotation", "y_rotation",
        "scores", "tag", "team",
        "name", "type", "predicate",
        "nbt", "level", "gamemode",
        "advancements", "limit", "sort"
    ], Any]