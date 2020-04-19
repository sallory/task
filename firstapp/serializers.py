from rest_framework import serializers
from .models import Human


class HumanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Human
        fields = '__all__'