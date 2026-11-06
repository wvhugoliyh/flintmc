from typing import TypeAlias

from flintmc.nodes.coordinate import Coordinate
from flintmc.nodes.entity import Entity
from flintmc.nodes.resource_location import ResourceLocation

NBTLocation: TypeAlias = Entity | Coordinate | ResourceLocation