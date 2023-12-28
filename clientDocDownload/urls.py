from django.urls import path
from . import views

urlpatterns = [
    path("", views.clientDownload, name='clientdownload'),
    # Add other patterns as needed
]