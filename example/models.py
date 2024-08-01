from django.db import models
from project.models import AbstractModel


class Color(AbstractModel):

    hex = models.CharField(max_length=7)
    name = models.CharField(blank=True, null=True)
    owner = models.ForeignKey(
        "access.User",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.name} {self.hex}" if self.name else self.hex
