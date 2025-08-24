from django.db import models

# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=130)
    year = models.IntegerField()
    genre = models.CharField(max_length=50)
    actor = models.ManyToManyField('Actor')

    def __str__(self):
        return self.name
    
class Actor(models.Model):
    name = models.CharField(max_length=130)
    birthdate = models.DateField()

    def __str__(self):
        return self.name
