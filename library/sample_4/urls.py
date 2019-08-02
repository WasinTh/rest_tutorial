from django.urls import path, include
from rest_framework.routers import DefaultRouter
from library.sample_4 import views


router = DefaultRouter()
router.register(r'author', views.AuthorViewSet)
router.register(r'book', views.BookViewset)


urlpatterns = [
    path('', include(router.urls)),
]
