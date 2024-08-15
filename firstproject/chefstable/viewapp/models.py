from django.db import models

# Create your models here.
class dress(models.Model):
    brand=models.CharField(max_length=50)
    price=models.IntegerField()
    color=models.CharField(max_length=10)
    
    