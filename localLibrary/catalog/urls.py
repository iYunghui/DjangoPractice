from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('books/', views.books, name="books"),
    path('authors/', views.author, name="author"),
    path('book/<int:id>', views.index),
    path('author/<int:id>', views.index),
]