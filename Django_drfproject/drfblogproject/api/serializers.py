from rest_framework import serializers
from .models import *

class CommnetSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields=['id','post','author','content','created_at']

class PostSerilizer(serializers.ModelSerializer):
    comment=CommnetSerializer(many=True, read_only=True)

    class Meta:
        model=Post
        fields=['id','title','author','content','created_at','comment']