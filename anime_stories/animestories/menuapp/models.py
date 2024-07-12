from django.db import models

# Create your models here.
class menu(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField()
    description=models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class booking(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    guest_number=models.IntegerField()
    comment=models.CharField(max_length=50)
    
    def __str__(self):
        return self.first_name+" "+self.last_name