from rest_framework import serializers
from errors.models import Error


class ErrorModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Error
        fields = ["id", "e_type", "e_msg", "application", "layer", "time"]
