from django.urls import path
from . import views

urlpatterns = [
    path("",views.home),
    path("detail/",views.details),
    path("getuser/<name>/<id>",views.getuser),
    path('getuser/', views.qryview, name='qryview') 
]
