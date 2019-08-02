from rest_framework import serializers
from library.models import Author, Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'name', 'author']


class AuthorSerializer(serializers.ModelSerializer):
    book_count = serializers.SerializerMethodField()

    def get_book_count(self, obj):
        return obj.book_set.count()

    class Meta:
        model = Author
        fields = ['id', 'name', 'book_count']
