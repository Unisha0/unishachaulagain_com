from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.blog_list, name='blog_list'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('blog/<slug:slug>/like/', views.like_post, name='like_post'),
    path('blog/<slug:slug>/comment/', views.add_comment, name='add_comment'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
]
