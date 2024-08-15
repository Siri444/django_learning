from django.shortcuts import render
from .models import dress
from .serializers import dress_serializer
from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,RetrieveAPIView,DestroyAPIView,ListCreateAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView
# Create your views here.

class dress_view(ListAPIView):
    queryset=dress.objects.all()
    serializer_class=dress_serializer
    
class create_view(CreateAPIView):
    queryset=dress.objects.all()
    serializer_class=dress_serializer
    
class retrieveview(RetrieveAPIView):
    queryset=dress.objects.all()
    serializer_class=dress_serializer
    
class updateview(UpdateAPIView):
    queryset=dress.objects.all()
    serializer_class=dress_serializer
    
class destroview(DestroyAPIView):
    queryset=dress.objects.all()
    serializer_class=dress_serializer
    
class dress_LC(ListCreateAPIView):
    queryset=dress.objects.all()
    serializer_class=dress_serializer
    
class dress_UR(RetrieveUpdateAPIView):
    queryset=dress.objects.all()
    serializer_class=dress_serializer
    
class dress_URD(RetrieveUpdateDestroyAPIView):
    queryset=dress.objects.all()
    serializer_class=dress_serializer