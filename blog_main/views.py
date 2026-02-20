from django.http import HttpResponse
from django.shortcuts import redirect, render
from blogs.models import Category, Blog
from snippets.models import About
from .forms import Registration_form
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth

# Homepage post function
def home(req):
    categories = Category.objects.all() 
    featured_post = Blog.objects.filter(is_featured=True, status = "Published").order_by('-updated_at')
    posts = Blog.objects.filter(is_featured = False, status = "Published")
    try:
        about = About.objects.get()
    except:
        about = None

    context =  {
        'categories': categories,
        'featured_post': featured_post,
        'posts': posts,
        'about': about,
    }
    return render(req, 'home.html', context)

# Registration 
def register(req):
    if req.method == 'POST':
        form = Registration_form(req.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
    else:
        form = Registration_form()
        # print('get req')
    context = {
        'form': form,
    }
    return render(req, 'register.html', context)


# Login function
def login(req):
    if req.method == 'POST':
        form = AuthenticationForm(req, req.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = auth.authenticate(username=username, password=password)
            
            if user is not None:
                auth.login(req, user)
               
            return redirect('dashboard')
    else:
        form = AuthenticationForm()

    context = {
        'form': form,
    }
    return render(req, 'login.html', context)

# Logout function

def logout(req):
    auth.logout(req)
    return redirect('home')