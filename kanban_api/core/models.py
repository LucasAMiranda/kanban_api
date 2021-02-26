from django.db import models


class Cards(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
