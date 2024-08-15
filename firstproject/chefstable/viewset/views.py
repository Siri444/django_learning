from django.shortcuts import render
from .models import icecream
from .serializers import iceserializer
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
# Create your views here.

class iceCRUD(viewsets.ViewSet):
    def list(self,request):
        ice=icecream.objects.all()
        serializer=iceserializer(ice,many=True)
        return Response(serializer.data)
    
    def retrieve(self,request,pk=None):
        id=pk
        if id is not None:
            ice=icecream.objects.get(id=id)
            serializer=iceserializer(ice)
            return Response(serializer.data)
    
    def create(self,request):
        serializer=iceserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Data Created'},status=status.HTTP_201_CREATED)
        return Response({'Invalid data'},status=status.HTTP_400_BAD_REQUEST)
    
    def update(self,request,pk=None):
        id=pk
        ice=icecream.objects.get(id=id)
        serializer=iceserializer(ice,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data updated'},status=status.HTTP_200_OK)
        return Response({'Invalid data'},status=status.HTTP_400_BAD_REQUEST)
     
    def partial_update(self,request,pk=None):
        id=pk
        ice=icecream.objects.get(id=id)
        serializer=iceserializer(ice,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'data updated'},status=status.HTTP_200_OK)
        return Response({'Invalid data'},status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self,request,pk):
        id=pk
        ice=icecream.objects.get(id=id)
        ice.delete()
        return Response({'Data deleted'})