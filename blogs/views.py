from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from blogs.models import Blog, Category

# Create your views here.

def posts_by_category(req, category_id):
    posts = Blog.objects.filter(status='Published', category_id=category_id)
    
    # use this when we want to redirect somewhere/do anything
    # try:
    #     category = Category.objects.get(id=category_id)
    # except:
    #     return redirect('home')

    #use this when we want to show 404 error page
    category = get_object_or_404(Category, id=category_id)
    context = {
        'posts': posts,
        'category_id': category,
    }
    return render(req, 'posts_by_catagory.html', context)
    