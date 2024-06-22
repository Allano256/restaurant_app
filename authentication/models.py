from django.db import models

# Create your models here.

class UserProfile(models.Model):
    username = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField()
    email = models.EmailField(max_length= 50)
   
    
