from django.db import models

# Create your models here.

class UserProfile(models.Model):
    usernaname = models.CharField(max_length=50)
    
