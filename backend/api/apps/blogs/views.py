from django.shortcuts import render, get_object_or_404
from .models import Blog
# Create your views here.
def index(request):
    blog = Blog.objects.order_by('title')
    data = {
        "blog_data" : blog,
    }
    return render(request, 'blogs/index.html', data)

def blog_page(request, id):
    obj = get_object_or_404(Blog, id=id)
    return render(request, 'blogs/blog_page.html', {'blog_page': obj})

