from dataclasses import dataclass

from flintmc.nodes import Node


@dataclass(slots=True)
class ResourceLocation(Node):
    namespace: str
    id: str

    def __repr__(self):
        return f"{self.namespace}:{self.id}"