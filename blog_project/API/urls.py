from django.urls import path
from .views import GetAllArticles, GetArticle, CreateArticle, test_api

urlpatterns = [
    path('articles/', GetAllArticles.as_view(), name='get_articles'),
    path('article/<int:pk>/', GetArticle.as_view(), name='get_article'),
    path('article/create/', CreateArticle.as_view(), name='create_article'),
    path('test-api/', test_api, name='test_api')
]