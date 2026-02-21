from .models import Category
from snippets.models import Social
from .models import Blog
# Category context processor
def get_catagories(req):
    categories = Category.objects.all()
    return dict(categories=categories)

# #Post context processor

# def get_posts(req):
#     posts = Blog.objects.all()
#     return dict(posts=posts)

# Social Link Context processor
def social_links(req):
    links = Social.objects.all()
    return dict(links=links)