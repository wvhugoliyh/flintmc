from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from flintmc.nodes import Coordinate, Entity, ResourceLocation

type NBTLocation = Entity | Coordinate | ResourceLocation