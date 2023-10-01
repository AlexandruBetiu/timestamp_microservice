from django.db import models


class Timestamp(models.Model):
    unix = models.BigIntegerField()
    utc = models.CharField(max_length=255)