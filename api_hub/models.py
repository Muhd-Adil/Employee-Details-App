from django.db import models

# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    address = models.CharField(max_length=255)
    department = models.CharField(max_length=100)
    joined_date = models.DateField()

    def __str__(self):
        return self.name
