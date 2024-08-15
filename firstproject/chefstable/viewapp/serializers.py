from rest_framework import serializers
from .models import dress


class dress_serializer(serializers.ModelSerializer):
    class Meta:
        model=dress
        fields=['brand','price','color']