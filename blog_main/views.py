from django.http import HttpResponse
from django.shortcuts import render
from blogs.models import Category, Blog
from snippets.models import About

def home(req):
    categories = Category.objects.all() 
    featured_post = Blog.objects.filter(is_featured=True, status = "Published").order_by('-updated_at')
    posts = Blog.objects.filter(is_featured = False, status = "Published")
    try:
        about = About.objects.get()
    except:
        about = none

    context =  {
        'categories': categories,
        'featured_post': featured_post,
        'posts': posts,
        'about': about,
    }
    return render(req, 'home.html', context)