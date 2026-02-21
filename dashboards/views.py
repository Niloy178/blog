from django.shortcuts import redirect, render, get_object_or_404
from blogs.models import Category, Blog
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm, BlogPostForm, UserForm, EditUserForm
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
# Create your views here.

#  Dashboards 

@login_required(login_url='login')
def dashboard(req):
    catagory_count = Category.objects.all().count()
    post_count = Blog.objects.all().count()
    context = {
        'catagory_count': catagory_count,
        'post_count': post_count,
    }
    return render(req, 'dashboard/dashboard.html', context)

def categories(req):
    return render(req, 'dashboard/categories.html')

# Add category
def add_category(req):
    if req.method == 'POST':
        form = CategoryForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
            
    form = CategoryForm()
    context={
        'form': form
    }
    return render(req, 'dashboard/add_category.html', context)

# Edit Category
def edit_category(req, id):
    category = get_object_or_404(Category, id=id)
    if req.method == 'POST':
        form = CategoryForm(req.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form = CategoryForm(instance=category)
    context = {
        'form': form,
        'category': category,
    }
    return render(req, 'dashboard/edit_category.html', context)

#  Delete category
def delete_category(req, id):
    category = get_object_or_404(Category, id=id)
    category.delete()
    return redirect('categories')


#Post CRUD Operations
# Posts
def posts(req):
    posts = Blog.objects.all()
    context = {
        'posts': posts
    }
    return render(req, 'dashboard/posts.html', context)

# Add Post
def add_post(req):
    if req.method == 'POST':
        form = BlogPostForm(req.POST, req.FILES)
        if form.is_valid():
            post = form.save(commit=False) #It will save temporury but not int db --
            post.author = req.user
            post.save() # We need to save it to get the post.id
            # slug = post.title.replace(' ', '-')
            title = form.cleaned_data['title']
            post.slug=slugify(title)+'-'+str(post.id) 
            post.save()
            return redirect('posts')

    form = BlogPostForm()
    context = {
        'form': form
    }
    return render(req, 'dashboard/add_post.html', context)


# Edit Post
def edit_post(req, id):
    post = get_object_or_404(Blog, id=id)
    if(req.method == 'POST'):
        form = BlogPostForm(req.POST, req.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            title = form.cleaned_data['title']
            post.slug = slugify(title)+'-'+str(post.id)
            post.save()
            return redirect('posts')
    
    form = BlogPostForm(instance=post)
    
    context = {
        'form': form
    }
    return render(req, 'dashboard/edit_post.html', context)

# delete Post 
def delete_post(req, id):
    post = get_object_or_404(Blog, id=id)
    post.delete()
    return redirect('posts')
    

# Users 
def users(req):
    users = User.objects.all()
    context = {
        'users': users,
    }
    return render(req, 'dashboard/users.html', context)
from django.http import HttpResponse
def add(req):
    if req.method == 'POST':
        form = UserForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
    
    form = UserForm()
    context = {
        'form': form,
    }
    return render(req, 'dashboard/add_user.html', context)


def delete_user(req, id):
    user = get_object_or_404(User, id=id)
    user.delete()
    return redirect('users')

def edit(req, id):
    user = get_object_or_404(User, id=id)
    if req.method == 'POST':
        form = EditUserForm(req.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users')
    form = EditUserForm(instance=user)
    context={
        'id': id,
        'form': form
    }
    return render(req, 'dashboard/edit_user.html', context)