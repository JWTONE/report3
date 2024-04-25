from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse
from .models import Article
from django.core import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ArticleSerializer


@api_view(["GET"])
def article_list(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    serializer = ArticleSerializer(article)
    return Response(serializer.data)