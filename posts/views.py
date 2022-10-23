from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    posts=Post.objects.all()
    content = {
        "posts": posts
    }
    return render(request, "index.html", content)

def post(request, pk):
    posts = Post.objects.get(id=pk)
    content = {
        "posts": posts
    }
    return render(request, "posts.html", content)