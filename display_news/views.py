import os
from django.shortcuts import render
import requests

API_KEY = os.environ.get("NEWS_API")

url = f"https://newsapi.org/v2/top-headlines?country=us&{API_KEY}"


def display(request):
	response = requests.get(url)
	articles = response.json()['articles']
	return render(request, 'display_news/display.html', {'articles':articles})
