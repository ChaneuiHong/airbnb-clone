from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import CharField
from django.utils.translation import LANGUAGE_SESSION_KEY

# Create your models here.
# AbstractUser 클래스를 상속
class Users(AbstractUser):

    """Custom User model"""

    # DB에 적재되는 데이터.
    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"
    # form에 보여질 데이터.
    GENDER_CHOICES = (
        (GENDER_FEMALE, "Female"),
        (GENDER_MALE, "Male"),
        (GENDER_OTHER, "Other"),
    )

    LANGUAGE_ENGLISH = "english"
    LANGUAGE_KOREAN = "korean"

    LANGUAGE_CHOICES = (
        (LANGUAGE_ENGLISH, "English"),
        (LANGUAGE_KOREAN, "Korean"),
    )

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"

    CURRENCY_CHOICES = ((CURRENCY_USD, "USD"), (CURRENCY_KRW, "KRW"))

    # field
    avatar = models.ImageField(upload_to="avatar", blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True)
    bio = models.TextField(default="")
    birthdate = models.DateField(null=True)
    language = CharField(choices=LANGUAGE_CHOICES, blank=True, max_length=10)
    currency = CharField(choices=CURRENCY_CHOICES, blank=True, max_length=3)
    superhost = models.BooleanField(default=False)
