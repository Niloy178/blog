from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    # Category CRUD url's
    path('categories/', views.categories, name='categories'),
    path('categories/add/', views.add_category, name='add_category'),
    path('categories/edit/<int:id>', views.edit_category, name='edit_category'),
    path('categories/delete/<int:id>', views.delete_category, name='delete_category'),

    # Post CRUD url's
    path('posts', views.posts, name='posts'),
    path('posts/delete/<int:id>', views.delete_post, name='delete_post'),
    path('posts/edit_post/<int:id>', views.edit_post, name='edit_post'),
    path('posts/add_post', views.add_post, name='add_post'),
]