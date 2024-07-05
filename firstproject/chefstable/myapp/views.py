from django.shortcuts import render
from django.http import HttpResponse
from myapp.form import inputform
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