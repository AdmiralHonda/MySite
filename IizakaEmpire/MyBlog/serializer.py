from rest_framework import serializers

from .models import Tag, Article

class TagEntry(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name','slug')


class ArticleEntry(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('slug', 'category', 'meta_description', 'ogp_title', 'ogp_img', 'pub_date')