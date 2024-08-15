from .models import student
from .serializers import studentserializer
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import BaseAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser
# Create your views here.

class studentCRUD(viewsets.ModelViewSet):
    queryset=student.objects.all()
    serializer_class=studentserializer
    authentication_classes=[SessionAuthentication]
    '''permission_classes=[IsAuthenticated]'''
    permission_classes=[IsAuthenticated]
    