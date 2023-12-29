from django.urls import path
from . import views

urlpatterns = [
    path("signin/", views.pos_signin, name='posauth'),
    path("file-upload/", views.file_upload, name='fileupload'),
    # Add other patterns as needed
]