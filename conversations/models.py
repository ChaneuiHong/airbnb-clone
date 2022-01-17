from django.db import models
from core import models as core_models


class Conversation(core_models.TimeStampModel):

    """Conversation Model Definition"""

    participants = models.ManyToManyField("users.Users", blank=True)

    def __str__(self):
        return f"{self.created}"


class Message(core_models.TimeStampModel):

    """Message Model Definition"""

    message = models.TextField()
    user = models.ForeignKey(
        "users.Users", related_name="messages", on_delete=models.CASCADE
    )
    conversation = models.ForeignKey(
        "Conversation", related_name="messages", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.user} says: {self.message}"