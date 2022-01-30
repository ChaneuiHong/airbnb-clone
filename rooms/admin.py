from django.contrib import admin
from django.db.models import fields
from django.utils.html import mark_safe
from . import models

# Register your models here.


@admin.register(models.RoomType, models.Amenity, models.Facility, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """Item Admin Definition"""

    list_display = (
        "name",
        "used_by",
    )

    def used_by(self, obj):
        return obj.rooms.count()


# Photo의 fk를 통해 Room에 사진 업로드 기능 구현
class RoomInline(admin.TabularInline):
    model = models.Photo


@admin.register(models.Room)
class RommAdmin(admin.ModelAdmin):

    """Room Admin Definition"""

    inlines = (RoomInline,)

    fieldsets = (
        (
            "Basic info",
            {"fields": ("name", "description", "country", "city", "address", "price")},
        ),
        (
            "Times",
            {"fields": ("check_in", "check_out", "instant_book")},
        ),
        ("Spaces", {"fields": ("guests", "beds", "bedrooms", "baths")}),
        (
            "More About The Spaces",
            {
                "classes": ("collapse",),
                "fields": (
                    "amenities",
                    "facilities",
                    "house_rules",
                ),
            },
        ),
        ("Last Details", {"fields": ("host",)}),
    )

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "address",
        "check_in",
        "check_out",
        "instant_book",
        "host",
        "room_type",
        "count_amenities",
        "count_photos",
        "total_rating",
    )

    list_filter = (
        "instant_book",
        "host__superhost",
        "amenities",
        "facilities",
        "house_rules",
        "city",
        "country",
    )

    filter_horizontal = (
        "amenities",
        "facilities",
        "house_rules",
    )

    #
    raw_id_fields = ("host",)

    search_fields = (
        "=city",
        "^host__username",
    )

    def count_amenities(self, obj):
        return obj.amenities.count()

    def count_photos(self, obj):
        return obj.photos.count()


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """Photo Admin Definition"""

    list_display = (
        "__str__",
        "get_thumbnail",
    )

    def get_thumbnail(self, obj):

        return mark_safe(f'<img width=100px src="{obj.files.url}"/>')

    get_thumbnail.short_description = "Thumbnail"
