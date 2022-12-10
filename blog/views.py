from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import (serializers, generics, status, views, permissions)
from rest_framework.response import Response

from drf_yasg.utils

from .models import Blog
from .serializers import SearchBlogSerializer
# Create your views here.
# create, update, list, search, delete

# search blog
class SearchBlogView(views.APIView):
    serializer_class = SearchBlogSerializer
    permission_classes = [permissions.AllowAny]

    responses = {
        status.HTTP_200_OK: SearchBlogSerializer,
        status.HTTP_400_BAD_REQUEST: 'Error'
    }

    @swagger_auto_schema(
        operation_summary=_("Search blogs and its info with filter keywords/ids"),
        security=[],
        responses=responses
    )

    def get(self, request):
        serializers= self.serializer_class(data=self.request.GET, context={'request': request})
        serializers.is_valid(raise_exception=True)

        title = serializers.validated_data.pop('title')
        try:
            blogs = None
            return Response('hellow world', status=status.HTTP_200_OK)
        except Exception as e:
            return Response('hellow world', status=status.HTTP_400_BAD_REQUEST)

    