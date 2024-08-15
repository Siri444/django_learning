from django.db import models

# Create your models here.
class menu(models.Model):
    name=models.CharField(max_length=20)
    cusine=models.CharField(max_length=20)
    price=models.IntegerField()
    
    def __str__(self):
        return self.name+':'+self.cusine
    
class student(models.Model):
    name=models.CharField(max_length=100)
    roll=models.IntegerField()
    city=models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
#for deserialization exampl

class employee(models.Model):
    emp_name=models.CharField(max_length=50)
    emp_id=models.IntegerField()
    department=models.CharField(max_length=50)
    
    def __str__(self):
        return self.emp_name
    
    
    
