from rest_framework import serializers
from newsapp.models import Country, Article


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        # fields = ('name', 'capital', 'continent', 'iso', 'code')
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'yes_vote', 'no_vote')
