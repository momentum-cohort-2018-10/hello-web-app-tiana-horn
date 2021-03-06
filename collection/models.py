from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Product(models.Model):
    price = models.FloatField()
    name = models.CharField(max_length=255)
    description = models.TextField()
    pictures = models.ImageField(upload_to='images/', null=True)
    slug = models.SlugField(unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE,
    blank=True, null=True)
