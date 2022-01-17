from django.db import models

# Create your models here.
class TimeStampModel(models.Model):

    """Time Stamped Model"""

    created = models.DateTimeField(auto_now_add=True)  # 모델이 생성된 날짜
    updated = models.DateTimeField(auto_now=True)  # 모델이 업데이트 될때마다

    class Meta:
        abstract = True
