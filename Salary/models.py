from django.db import models

# Create your models here.
class Employee(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    photo=models.CharField(max_length=100)
    designation=models.CharField(max_length=100)
    email_address=models.CharField(max_length=100)
    phone_number=models.CharField(max_length=100)
    Work_exp=models.CharField(max_length=100)