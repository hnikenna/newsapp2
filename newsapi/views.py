from rest_framework import viewsets

from .serializers import CountrySerializer, ArticleSerializer
from newsapp.models import Country, Article


class CountryViewset(viewsets.ModelViewSet):
    queryset = Country.objects.all().order_by('id')
    serializer_class = CountrySerializer


class ArticleViewset(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


