from django.contrib import admin
from .models import teacher

# Register your models here.
@admin.register(teacher)
class teacherAdmin(admin.ModelAdmin):
    list_display=['id','name','subject']