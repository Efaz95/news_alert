from django.shortcuts import render
import requests

url = ('https://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=a713ffa04e27486fb46b53ca2d9da630')


def display(request):
	response = requests.get(url)
	articles = response.json()['articles']
	return render(request, 'display_news/display.html', {'articles':articles})
