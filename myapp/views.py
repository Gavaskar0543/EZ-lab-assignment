from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import File
from .serializers import FileSerializer

class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer

    def create(self, request, *args, **kwargs):
       
        #file upload logic for Ops User
        try:
            # Your file upload logic here

            # Assuming you've validated the file type and saved it to the database
            return Response({"message": "File uploaded successfully"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request, *args, **kwargs):
        #list all the files in the db those uploaded by Ops user
        files = File.objects.all()
        serializer = FileSerializer(files, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
       
        #file download logic for Client User
        try:
            file_instance = self.get_object()
            # Assuming you generate a secure download link here
            download_link = f".../download-file/{file_instance.id}"
            return Response({"download-link": download_link, "message": "success"})
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
