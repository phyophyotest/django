from django.db import models
import datetime

# Create your models here.
# class Category(models.Model):
#     name=models.CharField(max_length=255)
#     created_at=models.DateTimeField(auto_now_add=True)

class Product(models.Model):
     name=models.CharField(max_length=225)
     price=models.IntegerField()
     image=models.ImageField()
     create_ad=models.DateTimeField(auto_now_add=True)
