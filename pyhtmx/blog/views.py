from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Blog

# Create your views here.
def index(request):
    latest_blogs = Blog.objects.order_by("-published")[:5]
    return render(request, "index.html", {"blogs": latest_blogs})

def blog(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, "detail.html", {"blog": blog})