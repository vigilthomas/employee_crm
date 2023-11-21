from django.db import models

# Create your models here.


class Employees(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    salary = models.PositiveBigIntegerField()
    email = models.EmailField(unique=True)
    dob = models.DateField(null=True)
    phone = models.IntegerField()
    profile_pic = models.ImageField(upload_to="crm/static/emp_img", null=True)

    def __str__(self):
        return "\n\n "+self.name + "\t"+self.email

