from django.shortcuts import render
from blog.models import Post


def home(request):
    posts = Post.objects.all()
    context = {'posts': posts, 'title': 'Homepage'}
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')
