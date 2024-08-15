from django.contrib import admin
from .models import drinks,students
# Register your models here.
admin.site.register(drinks)
@admin.register(students)
class studentsAdmin(admin.ModelAdmin):
    list_display=['id','student_name','roll','city']