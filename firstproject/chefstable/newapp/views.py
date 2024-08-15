from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import students
from .serializers import studentserializer
from rest_framework.views import APIView
from rest_framework import status
# Create your views here.
'''@api_view()
def student(request):
    return Response('function created')'''

'''@api_view(['GET'])
def student(request):
    return Response('function created')'''
    
'''@api_view(['POST','GET','PUT','DELETE'])
def student(request):
    if request.method=='POST':
        print(request.data)
        return Response('this a post method')
    if request.method=='GET':
        return Response("this is get method")'''


'''@api_view(['GET','POST','PUT','PATCH','DELETE'])
def student(request):
    if request.method=='GET':
        id=request.data.get('id')
        if id is not None:
            s=students.objects.get(id=id)
            serializer=studentserializer(s)
            return Response(serializer.data)
        s=students.objects.all()
        serializer=studentserializer(s,many=True)
        return Response(serializer.data)
    if request.method=='POST':
        serializer=studentserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("data created")
        return Response('data notvalid')
    if request.method=='PUT':
        id=request.data.get('id')
        stu=students.objects.get(pk=id)
        serializer=studentserializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('data modified')
        return Response('data not valid')
    if request.method=='PATCH':
        id=request.data.get('id')
        stu=students.objects.get(pk=id)
        serializer=studentserializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response('data modified')
        return Response('data not valid')
    if request.method=='DELETE':
        id=request.data.get('id')
        stu=students.objects.get(pk=id)
        stu.delete()
        return Response("data deleted")'''
        
        
class studentview(APIView):
    def get(self,request,pk=None,format=None):
        id=pk
        if id is not None:
            s=students.objects.get(id=id)
            serializer=studentserializer(s)
            return Response(serializer.data)
        s=students.objects.all()
        serializer=studentserializer(s,many=True)
        return Response(serializer.data)
    def post(self,request,format=None):
        serializer=studentserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors,status=status.HTTP_200_OK)
        return Response('data notvalid')
    def put(self,request,pk,format=None):
        id=pk
        stu=students.objects.get(pk=id)
        serializer=studentserializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('data modified')
        return Response('data not valid')
    def patch(self,request,pk,format=None):
        id=request.data.get('id')
        stu=students.objects.get(pk=id)
        serializer=studentserializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response('data modified')
        return Response('data not valid')
    def delete(self,request,pk,format=None):
        id=request.data.get('id')
        stu=students.objects.get(pk=id)
        stu.delete()
        return Response("data deleted")