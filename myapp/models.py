from django.db import models
from django.contrib.auth.models import User
#model to store file in the db
class File(models.Model):
    #when this user is removed from db, files which  are uploaded by this user also removed from db
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    filename = models.CharField(max_length=255)
    file_type = models.CharField(max_length=10)
    upload_date = models.DateTimeField(auto_now_add=True)
