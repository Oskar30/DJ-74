from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    image = models.ImageField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField()

