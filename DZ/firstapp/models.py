from django.db import models

class Cinema(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    subscription = models.IntegerField()

    def __str__(self):
        return self.name


class Film(models.Model):
    cinema = models.ForeignKey(Cinema, on_delete = models.CASCADE)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    price = models.IntegerField()
    genre = models.CharField(max_length=15)

    def __str__(self):
        return self.title

# Create your models here.
