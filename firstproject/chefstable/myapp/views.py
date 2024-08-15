import json
from django.shortcuts import render
from django.http import HttpResponse
from myapp.form import inputform
from .models import student,employee
from .serializers import studentserializer,employeeserializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io
from django.views.decorators.csrf import csrf_exempt 
# Create your views here.
def home(request):
    return HttpResponse("Hello welcome to the restraunt")
#string formatting and http response
def details(request):
    path= request.path
    scheme=request.scheme
    method=request.method
    address=request.META['REMOTE_ADDR']
    user_agent = request.META['HTTP_USER_AGENT']
    path_info=request.path_info 
    
    msg=f"""
        <br>path:{path} 
        <br>scheme:{scheme}
        <br>method:{method}
        <br>address:{address}
        <br>useragent:{user_agent}
        <br>pathinfo:{path_info}
    """
    response=HttpResponse(msg)
    return response

#working with urlparameters
def getuser(requet,name,id):
    return HttpResponse("Name:{} userid:{}".format(name,id))

#quering strings

def qryview(request):
    name=request.GET['name']
    id=request.GET['id']
    return HttpResponse("Name:{} userid:{}".format(name,id))
        
def formview(request):
    form=inputform()
    context={"form":form}
    return render(request,"home.html",context)

#templates

def menu(request):
    menuitem = {'name':"Greel_salad"}
    return render(request,'menu.html',menuitem)

#serializers

def student_detail(request,n):
    stu=student.objects.get(pk=n)
    serializer=studentserializer(stu)
    json_data=JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type='application/json')
    
    
#serializers query set
def student_list(request):
    stu=student.objects.all()
    serializer=studentserializer(stu, many=True)
    json_data=JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type='application/json')

#deserialization
@csrf_exempt
def employee_details(request):
    if request.method=='POST':
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        serializer=employeeserializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            msg={'msg':'data created'}
            json_data=JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
    
#CRUD operations
@csrf_exempt
def api_operations(request):
    if request.method=='GET':
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        id=python_data.get('id',None)
        if id is not None:
            data=student.objects.get(id=id)
            serializer=studentserializer(data)
            json_data=JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='application/json')
        data=student.objects.all()
        serializer=studentserializer(data,many=True)
        json_data=JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')
    if request.method=='POST':
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        serializer=studentserializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            msg={'msg':'datacreated'}
            json_data=JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
    if request.method=='PUT':
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        id=python_data.get('id')
        stu=student.objects.get(id=id)
        serializer=studentserializer(stu,data=python_data,partial=True)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'data modified'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
    if request.method=='DELETE':
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        id=python_data.get('id')
        stu=student.objects.get(id=id)
        stu.delete()
        res={'msg':'data deleted'}
        json_data=JSONRenderer().render(res)
        return HttpResponse(json_data,content_type='application/json')
        
            
            
        