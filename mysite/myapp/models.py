from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Color(models.Model):
    e = models.ForeignKey(Employee, on_delete=models.CASCADE)
    color = models.CharField(max_length=200)
    def __str__(self):
        return self.e.name + self.color
