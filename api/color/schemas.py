from ninja import Schema
from datetime import datetime
from typing import Any, Optional

from api.user.schemas import PublicUserOut


class ColorOut(Schema):
    id: int
    uuid: Any
    hex: str
    name: str
    created_at: datetime
    owner: Optional[PublicUserOut]


class ColorIn(Schema):
    hex: str
    name: str
