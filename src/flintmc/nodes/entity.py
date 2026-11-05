from typing import TypeAlias
from uuid import UUID

from flintmc.nodes import TargetSelector, Username

Entity: TypeAlias = TargetSelector | Username | UUID