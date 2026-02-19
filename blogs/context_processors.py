from .models import Category
from snippets.models import Social

# Category context processor
def get_catagories(req):
    categories = Category.objects.all()
    return dict(categories=categories)

# Social Link Context processor
def social_links(req):
    links = Social.objects.all()
    return dict(links=links)