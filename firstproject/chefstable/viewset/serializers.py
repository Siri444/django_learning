from rest_framework import serializers
from .models import icecream

class iceserializer(serializers.ModelSerializer):
    class Meta:
        model=icecream
        fields=['flavor','price']