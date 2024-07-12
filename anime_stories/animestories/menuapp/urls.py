from django.urls import path
from . import views
 
urlpatterns=[
    path("menu/",views.Menu,name='menu'),
    path('home/',views.home,name="home"),
    path('book/',views.booking,name="book"),
]