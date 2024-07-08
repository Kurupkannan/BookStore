from django.urls import path
from .views import add_book,get_all_books,book_detail
urlpatterns = [
    path('add', add_book, name='book-list-create'),
    path('all', get_all_books, name='get-all-books'),
    path('<int:pk>', book_detail, name='get-book')

    # path('books/<int:pk>/', book_detail, name='book-detail'),
    # path('authors/<int:pk>/books/', author_books, name='author-books'),
]   