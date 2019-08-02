from django.contrib import admin
from rest_framework.documentation import include_docs_urls
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', include_docs_urls()),
    path('library/', include('library.urls'))
]
