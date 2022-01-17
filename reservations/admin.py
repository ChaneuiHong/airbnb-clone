from django.contrib import admin
from . import models


@admin.register(models.Reservation)
class ReservationAdimn(admin.ModelAdmin):

    """Reservation Admin Definition"""

    pass
