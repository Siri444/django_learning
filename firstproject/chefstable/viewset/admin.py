from django.contrib import admin
from .models import icecream

# Register your models here.
@admin.register(icecream)
class icecreamAdmin(admin.ModelAdmin):
    list_display=['id','flavor','price']
