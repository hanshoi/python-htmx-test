from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Blog

def render_htmx(request, template, context=None, **kwargs):
    if request.htmx:
        base = "partial.html"
    else:
        base = "base.html"
    if context:
        context["base"] = base
    else:
        context = {"base": base}
    return render(request, template, context, **kwargs)

def index(request):
    return render_htmx(request, "index.html")

def about(request):
    return render_htmx(request, "about.html")

# Create your views here.
def blogs(request):
    latest_blogs = Blog.objects.order_by("-published")[:5]
    return render_htmx(request, "blogs.html", {"blogs": latest_blogs})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render_htmx(request, "detail.html", {"blog": blog})