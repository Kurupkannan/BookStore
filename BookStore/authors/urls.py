from django.urls import path
from .views import author_list_create, author_detail

urlpatterns = [
    path('add/', author_list_create, name='author-list-create'),
    path('authors/<int:pk>/', author_detail, name='author-detail'),
]
