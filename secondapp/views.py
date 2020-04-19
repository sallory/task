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

    def get(self, request):
        matches = Match.objects.all().order_by('created_at')
        host = request.get_host()
        response = requests.get(url=f'http://{host}/api/human/')
        humans = json.loads(response.text)
        for match in matches:
            try:
                human = next(human for human in humans if human["id"] == match.human_id)
            except:
                human = None
            match.human = human
        paginator = LimitOffsetPagination()
        result_page = paginator.paginate_queryset(matches, request)
        serializer = MatchSerializer(result_page, many=True, context={'request':request})
        response = Response(serializer.data, status=status.HTTP_200_OK)
        return response


class match(APIView):

    def get(request, data, human_id):
        match = get_object_or_404(Match, human_id=human_id)
        serializer = MatchSerializer(match)
        return Response(serializer.data)


