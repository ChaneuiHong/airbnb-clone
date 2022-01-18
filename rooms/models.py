from django.db import models
from django.db.models.fields import CommaSeparatedIntegerField
from django_countries.fields import CountryField
from core import models as core_models


# Create your models here.


class AbstractItem(core_models.TimeStampModel):

    """Abstract Iten"""

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):

    """Room Type Model Definition"""

    class Meta:
        verbose_name = "Room Type"


class Amenity(AbstractItem):

    """Amenity Model Definition"""

    class Meta:
        verbose_name_plural = "Amenities"


class Facility(AbstractItem):

    """Facility Model Definition"""

    class Meta:
        verbose_name_plural = "Facilities"


class HouseRule(AbstractItem):

    """HouseRule Model Definition"""

    class Meta:
        verbose_name_plural = "House Rules"


class Photo(AbstractItem):

    """Photo Model Definition"""

    caption = models.CharField(max_length=80)
    files = models.ImageField()
    room = models.ForeignKey("Room", related_name="photos", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


class Room(core_models.TimeStampModel):

    """Room Model Definition"""

    name = models.CharField(max_length=100)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)

    # foreign key
    host = models.ForeignKey(
        "users.Users", related_name="rooms", on_delete=models.CASCADE
    )
    room_type = models.ForeignKey(
        "RoomType", related_name="rooms", on_delete=models.SET_NULL, null=True
    )

    # many to manyㅁ
    amenities = models.ManyToManyField("Amenity", related_name="rooms", blank=True)
    facilities = models.ManyToManyField("Facility", related_name="rooms", blank=True)
    house_rules = models.ManyToManyField("HouseRule", related_name="rooms", blank=True)

    # __str__: 객체를 string 타입으로 보여줌?
    def __str__(self):
        return self.name

    # room에 달린 Reivew의 평균
    def total_rating(self):
        # fk의 모든 reviews 객체를 가져옴
        all_reviews = self.reviews.all()
        all_ratings = 0
        for review in all_reviews:
            all_ratings += review.rating_average()
        return round(all_ratings / len(all_reviews), 2)
