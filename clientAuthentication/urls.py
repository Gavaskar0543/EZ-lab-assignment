from django.urls import path
from . import views

urlpatterns = [
    path("", views.clientauth, name='posauth'),
    # Add other patterns as needed
]