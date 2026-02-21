from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from blogs.models import Blog, Category, Comment
from django.db.models import Q
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


# Single Post
def blog_post_view(req, post_slug):
    # post = Blog.objects.get(slug=post_slug)
    post = get_object_or_404(Blog, slug=post_slug, status='Published')
    if(req.method == 'POST'):
        comment = Comment()
        comment.user = req.user
        comment.blog = post
        comment.comment = req.POST['comment']
        comment.save()
        return HttpResponseRedirect(req.path_info)

    # Comments
    comments = Comment.objects.filter(blog=post)
    context = {
        'post': post,
        'comments': comments, 
    }
    return render(req, 'blog_posts.html', context)

# Search function
def search(req):
    keyword = req.GET.get('keyword')
    blogs = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword), status = 'Published')
    context = {
        'blogs': blogs,
        'keyword': keyword,
    }
    return render(req, 'search.html', context)