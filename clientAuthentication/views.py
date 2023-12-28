
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

def signup(request):
    if request.user.is_authenticated:
        return redirect('/')  # Redirect to the home page if the user is already authenticated

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')  # Use 'password1' as it contains the password
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('/')  # Redirect to the home page after successful signup
    else:
        form = UserCreationForm()

    return redirect('client/login')

def signin(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return redirect('/')
    return redirect('/')
