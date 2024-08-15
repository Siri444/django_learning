from django.contrib import admin
from django.urls import path,include
from modelviewset import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register('teacherapi',views.teacherreadonlymodelviewset,basename='teacher')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
]