from django.urls import path
from . import views

urlpatterns = [
    path("", views.posupload, name='posupload'),
    # Add other patterns as needed
]