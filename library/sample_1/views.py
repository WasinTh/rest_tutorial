import json
from django.http import HttpResponse
from django.views import View
from django.shortcuts import get_object_or_404
from library.models import Author, Book


class AuthorList(View):
    def get(self, request):
        response = list()
        for author in Author.objects.all():
            response.append({
                'id': author.id,
                'name': author.name
            })
        return HttpResponse(json.dumps(response), content_type='application/json')


class AuthorDetail(View):
    def get(self, request, id):
        author = get_object_or_404(Author, id=id)
        response = {
            'id' : author.id,
            'name': author.name
        }
        return HttpResponse(json.dumps(response), content_type='application/json')


class BookDetail(View):
    def get(self, request, id):
        book = get_object_or_404(Book, id=id)
        response = {
            'id': book.id,
            'name': book.name,
            'author': {
                'id': book.author.id,
                'name': book.author.name
            }
        }
        return HttpResponse(json.dumps(response), content_type='application/json')


class BookList(View):
    def get(self, request):
        response = list()
        for book in Book.objects.all():
            response.append({
                'id': book.id,
                'name': book.name,
                'author': {
                    'id': book.author.id,
                    'name': book.author.name
                }
            })
        return HttpResponse(json.dumps(response), content_type='application/json')