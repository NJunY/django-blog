from rest_framework import serializers
from .models import Blog
from user.models import User

class SearchBlogSerializer(serializers.Serializer):
    title = serializers.CharField(write_only=True, required=False)
    