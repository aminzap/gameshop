from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    thumbnail = models.ImageField(upload_to='./thumbnail')
    user_name=models.ForeignKey(User,on_delete=models.CASCADE,default=1)