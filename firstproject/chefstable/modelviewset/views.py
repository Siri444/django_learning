from django.shortcuts import render
from .models import teacher
from .serializers import teacherserializer
from rest_framework import viewsets
# Create your views here.
class teachermodelviewset(viewsets.ModelViewSet):
    queryset=teacher.objects.all()
    serializer_class=teacherserializer
    
class teacherreadonlymodelviewset(viewsets.ReadOnlyModelViewSet):
    queryset=teacher.objects.all()
    serializer_class=teacherserializer