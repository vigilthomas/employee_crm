from django.db import models

# Create your models here.
class Employees(models.Model):
    name=models.CharField(max_length=100)
    department=models.CharField(max_length=100)
    salary=models.PositiveBigIntegerField()
    email=models.EmailField(unique=True)
    age=models.PositiveBigIntegerField()
    phone=models.IntegerField()

    def __str__(self) :
        return "\n "+self.name+"\n "+ self.email+" \n\n"

