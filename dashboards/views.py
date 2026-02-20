from django.shortcuts import redirect, render, get_object_or_404
from blogs.models import Category, Blog
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm


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
    category = get_object_or_404(Category, id=id).delete()
    return redirect('categories')