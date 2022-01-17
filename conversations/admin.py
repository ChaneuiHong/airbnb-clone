from django.contrib import admin
from . import models


@admin.register(models.Conversation)
class ConversationsAdmin(admin.ModelAdmin):

    """Conversation Admin Defisition"""

    pass


@admin.register(models.Message)
class MessagesAdmin(admin.ModelAdmin):

    """Conversation Admin Defisition"""

    pass
