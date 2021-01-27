from django.urls import path,include

urlpatterns = [
    path('',include('mainapp.urls')),
]
