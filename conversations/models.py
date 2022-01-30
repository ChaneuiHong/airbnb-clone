from django.db import models
from core import models as core_models


class Conversation(core_models.TimeStampModel):

    """Conversation Model Definition"""

    participants = models.ManyToManyField("users.Users", blank=True)

    def __str__(self):
        usernames = []
        for user in self.participants.all():
            usernames.append(user.username)
        return ", ".join(usernames)

    # fk 이용하여 messgae 가져오기
    def count_messages(self):
        return self.messages.count()

    count_messages.short_description = "Number of Messages"


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
