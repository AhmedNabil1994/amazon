from django.shortcuts import render
from pages.models import Myusers
from rest_framework import viewsets,status
from .serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
class Userslist(viewsets.ModelViewSet):
    queryset = Myusers.objects.all()
    serializer_class = UserSerializer

@api_view(['PUT','DELETE'])

def usersOperations(request,pk):
    
    if request.method == 'PUT':
        serializer = UserSerializer(Myusers, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

