from rest_framework import serializers

from .models import Articles


class ArticlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = ['article_id', 'category', 'title', 'content', 'status']
