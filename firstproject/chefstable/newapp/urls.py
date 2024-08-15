from django.urls import path
from . import views

urlpatterns = [
    path("student/",views.studentview.as_view()),
    path("student/<int:pk>",views.studentview.as_view()),
]
