from ninja import Router
from ninja.pagination import paginate

from example.models import Color
from .schemas import ColorIn, ColorOut
from api.pagination import DefaultPagination


router = Router()


@router.get("/", response=list[ColorOut])
@paginate(DefaultPagination)
def color_list(request):
    queryset = Color.objects.all()
    return list(queryset)


@router.post("/", response=ColorOut)
def color_create(request, data: ColorIn):
    color = Color.objects.create(**data.dict())
    return color
