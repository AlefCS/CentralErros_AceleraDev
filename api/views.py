from django.shortcuts import render
from rest_framework import viewsets
from api.serializers import ErrorModelSerializer
from errors.models import Error


# Create your views here.
class ErrorAPIViewSet(viewsets.ModelViewSet):
    queryset = Error.objects.all()
    serializer_class = ErrorModelSerializer
