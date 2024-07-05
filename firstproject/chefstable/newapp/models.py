from django.db import models

# Create your models here.
    
class drinks(models.Model):
    name=models.CharField(max_length=50)
    type=models.CharField(max_length=50,default='hot')
    price=models.IntegerField()
    
    def __str__(self):
        return self.name