from ninja.pagination import PageNumberPagination
from ninja import Schema
from typing import Any


class DefaultPagination(PageNumberPagination):

    class Input(Schema):
        limit: int = 10
        page: int = 1

    class Output(Schema):
        count: int
        page: int
        limit: int
        results: list[Any]

    items_attribute: str = "results"

    def paginate_queryset(self, queryset, pagination: Input, **params):
        offset = (pagination.page - 1) * pagination.limit
        print(offset)
        return {
            "count": self._items_count(queryset),
            "page": pagination.page,
            "limit": pagination.limit,
            "results": queryset[offset : offset + self.page_size],
        }
