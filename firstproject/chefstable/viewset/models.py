from django.db import models

# Create your models here.
class icecream(models.Model):
    flavor=models.CharField(max_length=20)
    price=models.IntegerField()
    