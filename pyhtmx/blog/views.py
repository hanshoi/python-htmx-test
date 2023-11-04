from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Blog

def index(request):
    return render(request, "index.html")

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

# Create your views here.
def blogs(request):
    latest_blogs = Blog.objects.order_by("-published")[:5]
    return render(request, "blogs.html", {"blogs": latest_blogs})

def blog(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, "detail.html", {"blog": blog})