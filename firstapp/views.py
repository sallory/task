from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import LimitOffsetPagination
from faker import Faker

from .models import Human
from .serializers import HumanSerializer
import requests
import random

# Create your views here.

class humans(APIView):

    def post(self, request):
        serializer = HumanSerializer(data=request.data)
        if serializer.is_valid():
            human = serializer.save()
            fake = Faker()
            match = {
                'first_name': fake.first_name(),
                'second_name': fake.last_name(),
                'age': random.randrange(100),
                'human_id': human.id,
                'gender': random.choice(['male', 'famale']),
            }
            host = request.get_host()
            requests.post(url=f'http://{host}/api/match/', json=match)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def get(self, request):
        humans = Human.objects.all().order_by('created_at')
        paginator = LimitOffsetPagination()
        result_page = paginator.paginate_queryset(humans, request)
        serializer = HumanSerializer(result_page, many=True, context={'request':request})
        response = Response(serializer.data, status=status.HTTP_200_OK)
        return response


class human(APIView):

    def get(self, request, id):
        human = get_object_or_404(Human, id=id)
        serializer = HumanSerializer(human)
        return Response(serializer.data)

    
    def put(self, request, id):
        human = get_object_or_404(Human, id=id)
        serializer = HumanSerializer(human, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def delete(self, request, id):
        human = get_object_or_404(Human, id=id)
        human.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
