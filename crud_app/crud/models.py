from django.db import models

# Create your models here.

class Person(models.Model):
    fname  = models.CharField(max_length=200)
    lname  = models.CharField(max_length=200)
    age    = models.IntegerField()