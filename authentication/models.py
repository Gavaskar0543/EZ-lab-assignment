from django.db import models
from django.contrib.auth.models import User

class UploadedFile(models.Model):
    id = models.BigAutoField(primary_key=True)
    filename = models.CharField(max_length=255)
    file_type = models.CharField(max_length=10)
    upload_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.filename
