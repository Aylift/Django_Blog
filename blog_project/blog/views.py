from django.shortcuts import render
from django.http import HttpResponse


POSTS = [
    {
        'author': 'Aylift',
        'title': 'To be or not to be',
        'content': 'First post',
        'date': '3 Feb 2025'
    },
    {
        'author': 'Aylift',
        'title': 'Lorem ipsum',
        'content': 'Second post',
        'date': '4 Feb 2025'
    }
]

def home(request):
    return render(request, 'blog/home.html', {'title': 'Home', 'posts': POSTS})

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})