import orjson
from ninja import NinjaAPI
from .renderer import ORJSONRenderer

router = NinjaAPI(renderer=ORJSONRenderer())
router.add_router("/auth/", "api.auth.views.router")
router.add_router("/color/", "api.color.views.router")
