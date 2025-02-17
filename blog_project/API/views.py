from django.shortcuts import render
from rest_framework.viewsets import generics
from .serializers import ArticleSerializer
from blog.models import Article


class GetAllArticles(generics.ListAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()


class GetArticle(generics.RetrieveAPIView):
    serializer_class = ArticleSerializer
    queryset = Article


class CreateArticle(generics.CreateAPIView):
    serializer_class = ArticleSerializer

def test_api(request):
    return render(request, 'API/test-api.html')