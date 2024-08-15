from django.contrib import admin
from .models import menu,student,employee
# Register your models here.
admin.site.register(menu)
admin.site.register(employee)
@admin.register(student)
class studentAdmin(admin.ModelAdmin):
    list_display=['name','roll','city']
