from django.urls import path
from library.sample_3 import views

urlpatterns = [
    path('author', views.AuthorList.as_view()),
    path('author/<int:id>', views.AuthorDetail.as_view()),
    path('book', views.BookList.as_view()),
    path('book/<int:pk>', views.BookDetail.as_view())
]
