from django.urls import path
from . import views
urlpatterns = [
    path('', views.blog_index, name = 'blog_index'),
    path('<slug:slug>', views.blog_detail, name = 'blog_detail')
]