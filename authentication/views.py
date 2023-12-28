
from django.shortcuts import render
from django.http import JsonResponse

def auth(request):
    data = {'message': 'auth!'}
    return JsonResponse(data)
   

