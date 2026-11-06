from typing import TypeAlias
from uuid import UUID

from flintmc.nodes.target_selector import TargetSelector
from flintmc.nodes.username import Username

Entity: TypeAlias = TargetSelector | Username | UUID