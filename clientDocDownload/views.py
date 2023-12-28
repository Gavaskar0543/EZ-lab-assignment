from django.shortcuts import render

from django.http import HttpResponse

def clientDownload(request):
    return HttpResponse("client download")