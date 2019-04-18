from django.shortcuts import render
from .models import Post

def blog(request):
    context={}
    posts = Post.objects.all()
    context['posts'] = posts
    return render(request, 'blog/blog.html',context)
