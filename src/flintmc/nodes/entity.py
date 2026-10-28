from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from uuid import UUID
    
    from flintmc.nodes import TargetSelector, Username

type Entity = TargetSelector | Username | UUID