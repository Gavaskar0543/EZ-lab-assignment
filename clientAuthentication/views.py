from django.shortcuts import render

from django.http import HttpResponse

def clientauth(request):
    return HttpResponse("client auth")