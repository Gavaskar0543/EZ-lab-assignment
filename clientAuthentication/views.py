from contextlib import _RedirectStream
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])  # Use appropriate authentication classes
@permission_classes([AllowAny])  # Allow any user, including unauthenticated ones
def signup(request):
    if request.user.is_authenticated:
        return Response({'detail': 'User is already authenticated.'}, status=400)

    if request.method == 'POST':
        form = UserCreationForm(request.data)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')  # Use 'password1' as it contains the password
            email = form.cleaned_data.get('email')
            
            print(username,password,email)
            user = authenticate(request, username=username, password=password, email=email)
            if user:
                login(request, user)
                return Response({'detail': 'Signup successful.'})
        else:
            print(form.errors)
            return Response({'detail': 'Invalid form data.'}, status=400)

    return Response({'detail': 'Method not allowed.'}, status=405)


@csrf_exempt  # Disabling CSRF protection for demonstration purposes (not recommended in production)
def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Log in the user
            login(request, user)
            return JsonResponse({'detail': 'Login successful.'})
        else:
            return JsonResponse({'detail': 'Invalid username or password.'}, status=401)

    return JsonResponse({'detail': 'Method not allowed.'}, status=405)
