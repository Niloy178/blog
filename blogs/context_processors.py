from .models import Category

def get_catagories(req):
    categories = Category.objects.all()
    return dict(categories=categories)