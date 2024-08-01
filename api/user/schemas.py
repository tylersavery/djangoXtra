from ninja import Schema
from datetime import datetime


from access.models import User


class PublicUserOut(Schema):
    username: str
    first_name: str
    last_name: str
    date_joined: datetime
