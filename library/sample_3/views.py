from rest_framework import generics
from library.models import Author, Book
from library.sample_3.serializers import AuthorSerializer, BookSerializer


class AuthorList(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    lookup_field = 'id'
    serializer_class = AuthorSerializer


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        return Book.objects.filter(id=self.kwargs.get('pk', None))

    serializer_class = BookSerializer


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer