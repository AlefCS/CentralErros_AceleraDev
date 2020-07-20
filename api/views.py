from django.shortcuts import render
from rest_framework import viewsets, mixins
from api.serializers import ErrorModelSerializer
from errors.models import Error


# Create your views here.
class ErrorAPIViewSet(mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.DestroyModelMixin,
                      mixins.ListModelMixin,
                      viewsets.GenericViewSet):
    queryset = Error.objects.all()
    serializer_class = ErrorModelSerializer


def show_docs(request):
    return render(request, "swagger.html")
