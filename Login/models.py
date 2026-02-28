from django.db import models

# Create your models here.

class Designation(models.Model):
    name=models.CharField(max_length=10)
    def __str__(self):
        return self.name

class UserRegistration(models.Model):
    username=models.CharField(max_length=100)
    designation=models.ForeignKey(Designation,on_delete=models.CASCADE)
    salary=models.CharField(max_length=10000)
    created_at=models.DateTimeField(auto_now_add=True)
    password=models.CharField(max_length=10)
    confirm_password=models.CharField(max_length=10)
    def __str__(self):
        return self.username

