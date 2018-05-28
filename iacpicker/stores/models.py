from django.db import models
from django.db.models.aggregates import Count
from random import randint

# Create your models here.
class StoreManager(models.Manager):
    def random(self):
        count = self.aggregate(count=Count('id'))['count']
        random_index = randint(0, count - 1)
        return self.all()[random_index]

class Store(models.Model):
    objects = StoreManager()
    name = models.CharField(max_length = 50)
    description = models.TextField()
    image = models.CharField(max_length = 50)
    location = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Stores"
