from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(default='profile_picture/default/profilepic.png',upload_to='profile_picture')
    city=models.CharField(max_length=22)

