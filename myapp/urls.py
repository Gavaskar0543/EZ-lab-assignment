
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('pos/authentication/', include('authentication.urls')),
    path('client/authentication/', include('clientAuthentication.urls')),
    path('client/download/', include('clientDocDownload.urls')),
    path('pos/upload/', include('posDocUpload.urls')),
]