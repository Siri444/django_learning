from django.urls import path
from . import views

urlpatterns = [
    path("",views.home),
    path("detail/",views.details),
    path("getuser/<name>/<id>",views.getuser),
    path('getuser/', views.qryview, name='qryview'),
    path("home/",views.formview, name="formview"),
    path('menu/',views.menu),
    path('student/<int:n>',views.student_detail),
    path('info/',views.student_list),
    path('empinfo/',views.employee_details),
    path('studentapi/',views.api_operations),
]
