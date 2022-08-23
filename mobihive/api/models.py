from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    
    profile_photo  = models.ImageField(upload_to='profile_pic', null=True, blank=True)
    address =  models.CharField(max_length=250,null=True,blank=True)
    phone_no = models.CharField(max_length=100,null=True,blank=True)
    city = models.CharField(max_length=100,null=True,blank=True)
