from django.db import models

# Create your models here.
    
class drinks(models.Model):
    name=models.CharField(max_length=50)
    type=models.CharField(max_length=50,default='hot')
    price=models.IntegerField()
    
    def __str__(self):
        return self.name
    
class students(models.Model):
    student_name=models.CharField(max_length=50)
    roll=models.IntegerField()
    city=models.CharField(max_length=50)
    
    def __str__(self):
        return self.student_name