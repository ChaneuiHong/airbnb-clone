from tkinter import HORIZONTAL
from django.contrib import admin
from . import models


@admin.register(models.Conversation)
class ConversationsAdmin(admin.ModelAdmin):

    """Conversation Admin Defisition"""

    list_display = (
        "__str__",
        "count_messages",
    )

    filter_horizontal = ("participants",)


@admin.register(models.Message)
class MessagesAdmin(admin.ModelAdmin):

    """Conversation Admin Defisition"""

    list_display = (
        "__str__",
        "created",
    )
