from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Article
from django.core import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ArticleSerializer

