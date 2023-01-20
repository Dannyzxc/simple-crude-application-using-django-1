from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField( max_length=50)
    phone = models.CharField( max_length=50)
    email = models.CharField( max_length=50)
    address = models.CharField( max_length=50)
    creaded = models.DateField(auto_now=True)
    born = models.DateField()

    def __str__(self):
        return self.name