from django.db import models

# Create your models here.
class Employees(models.Model):
    name=models.CharField(max_length=100)
    department=models.CharField(max_length=100)
    salary=models.PositiveBigIntegerField(max_length=100)
    email=models.EmailField(unique=True)
    age=models.PositiveBigIntegerField(null=True)
    phone=models.IntegerField(max_length=10)

