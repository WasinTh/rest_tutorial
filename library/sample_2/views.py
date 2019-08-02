from django.views import View
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from library.models import Author, Book
from library.sample_2.serializers import AuthorSerializer, BookSerializer


class AuthorList(View):
    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return JsonResponse(serializer.data, safe=False)


class AuthorDetail(View):
    def get(self, request, id):
        author = get_object_or_404(Author, id=id)
        serializer = AuthorSerializer(author)
        return JsonResponse(serializer.data)


class BookDetail(View):
    def get(self, request, id):
        book = get_object_or_404(Book, id=id)
        serializer = BookSerializer(book)
        return JsonResponse(serializer.data)


class BookList(View):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return JsonResponse(serializer.data, safe=False)
