from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view, authentication_classes , permission_classes
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse
from .models import UploadedFile
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import UploadedFile

from django.contrib.auth.decorators import login_required
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





@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def file_upload(request):
    if request.method == 'POST':
        # Check if the user is staff
        if not request.user.is_staff:
            return Response({'detail': 'Staff permission required for file upload.'}, status=403)

        # Handle file upload logic only if is_staff is True
        if request.user.is_staff:
            file = request.FILES.get('file')
            if not file:
                return Response({'detail': 'File not provided.'}, status=400)

            allowed_extensions = ['pptx', 'docx', 'xlsx']
            if file.name.split('.')[-1].lower() not in allowed_extensions:
                return Response({'detail': 'Invalid file type. Allowed types: pptx, docx, xlsx.'}, status=400)

            uploaded_file = UploadedFile(user=request.user)
            uploaded_file.file.save(file.name, file)

            return Response({'detail': 'File uploaded successfully.'})
        else:
            return Response({'detail': 'User does not have permission to upload files.'}, status=403)

    return Response({'detail': 'Method not allowed.'}, status=405)
