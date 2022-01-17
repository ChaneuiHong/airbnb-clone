from django.db import models
from core import models as core_models


class List(core_models.TimeStampModel):

    """List Model Definition"""

    name = models.CharField(max_length=80)

    # FK
    user = models.ForeignKey(
        "users.Users", related_name="lists", on_delete=models.CASCADE
    )
    # many to many
    rooms = models.ManyToManyField("rooms.Room", related_name="lists", blank=True)

    def __str__(self):
        return self.name
