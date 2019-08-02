from django.urls import path, include

urlpatterns = [
    path('sample_1/', include('library.sample_1.urls')),
    path('sample_2/', include('library.sample_2.urls')),
    path('sample_3/', include('library.sample_3.urls')),
    path('sample_4/', include('library.sample_4.urls')),
]
