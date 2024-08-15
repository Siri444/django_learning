from rest_framework import serializers
from .models import students

class studentserializer(serializers.ModelSerializer):
    class Meta:
        model=students
        fields=['id','student_name','roll','city']