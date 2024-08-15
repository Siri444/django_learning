from django.contrib import admin
from .models import dress
# Register your models here.
@admin.register(dress)
class dressAdmin(admin.ModelAdmin):
    list_display=['id','brand','price','color']