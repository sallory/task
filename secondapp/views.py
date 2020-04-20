from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import LimitOffsetPagination

from .models import Match
from .serializers import MatchSerializer

import requests
import json


class matches(APIView):

    def post(self, request):
        serializer = MatchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def get(self, request):
        matches = Match.objects.all().order_by('created_at')
        host = request.get_host()
        paginator = LimitOffsetPagination()
        result_page = paginator.paginate_queryset(matches, request)
        for match in result_page:
            response = requests.get(url=f'http://{host}/api/human/{match.human_id}')
            human = json.loads(response.text)
            match.human = human
        serializer = MatchSerializer(result_page, many=True, context={'request':request})
        response = Response(serializer.data, status=status.HTTP_200_OK)
        return response


class match(APIView):

    def get(request, data, human_id):
        match = get_object_or_404(Match, human_id=human_id)
        serializer = MatchSerializer(match)
        return Response(serializer.data)


