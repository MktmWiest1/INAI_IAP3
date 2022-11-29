from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=155)
    description = models.TextField(null=True)
    image = models.ImageField(null=True)
    genre = models.CharField(max_length=100)
    country = models.CharField(max_length=150)
    duration = models.DurationField(null=True)



