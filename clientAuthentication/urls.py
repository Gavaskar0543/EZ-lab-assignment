from django.urls import path
from . import views

urlpatterns = [
    path("client/signup", views.signup, name='clientauthsignup'),
    path("client/login", views.signin, name='clientauthsignin'),

    # Add other patterns as needed
]