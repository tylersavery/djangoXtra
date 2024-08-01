import orjson
from ninja.renderers import BaseRenderer
from django.http import HttpRequest
from typing import Any


class ORJSONRenderer(BaseRenderer):
    media_type = "application/json"

    def render(self, request: HttpRequest, data: Any, *, response_status: int):
        return orjson.dumps(data)
