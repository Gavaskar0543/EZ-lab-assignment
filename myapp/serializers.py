from rest_framework import serializers
from .models import File
""""serialize the file automatically"""
class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['id', 'file_name', 'file_type', 'upload_date']
