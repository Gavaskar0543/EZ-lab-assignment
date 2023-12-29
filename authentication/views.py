from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.contrib.auth.forms import AuthenticationForm

@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
def pos_signin(request):
    if request.user.is_authenticated:
        return Response({'detail': 'User is already authenticated.'}, status=400)

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.data)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                return Response({'detail': 'Login successful.'})
            else:
                
                return Response({'detail': 'Invalid username or password or user not authorized.'}, status=400)

        else:
            print(form.errors)
            return Response({'detail': 'Invalid username or password.'}, status=400)

    return Response({'detail': 'Method not allowed.'}, status=405)
