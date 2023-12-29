from django.urls import path
from . import views

urlpatterns = [
    path("signin/", views.pos_signin, name='posauth'),
    # Add other patterns as needed
]