from rest_framework import serializers

from .models import Match


class HumanSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    avatar = serializers.CharField()
    first_name = serializers.CharField()
    second_name = serializers.CharField()
    age = serializers.IntegerField()
    gender = serializers.CharField()


class MatchSerializer(serializers.ModelSerializer):
    human = HumanSerializer(required=False)

    class Meta:
        model = Match
        fields = '__all__'