from rest_framework.viewsets import generics
from .serializers import ArticleSerializer
from blog.models import Article

class GetAllArticles(generics.ListAPIView): # dziediczący widok może korzystać z metody GET, dostęp read-only
    serializer_class = ArticleSerializer # przekształca obiekty z bazy do JSON-a
    queryset = Article.objects.all() # po wykonaniu zapytania na endpoint-cie, serializowana ma być lista wszystkich artykułów
