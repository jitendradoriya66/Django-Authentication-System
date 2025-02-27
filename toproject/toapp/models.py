from django.db import models

# Create your models here.

    
class registeration(models.Model):
    fullname=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=15)
    password=models.CharField(max_length=128)
    c_password=models.CharField(max_length=128)
    otp=models.IntegerField(blank=True,null=True)
    def __str__(self):
        return self.fullname
    
    
class rate(models.Model):
    star=models.IntegerField()
    
    