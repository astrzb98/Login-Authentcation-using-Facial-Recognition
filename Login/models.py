from django.core.files.storage import FileSystemStorage
from django.db import models
from django.contrib.auth.models import User


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return '{0}/{1}'.format(instance.username, filename)

class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    mail = models.CharField(max_length=100,unique=True)
    username = models.CharField(max_length=100,unique=True)
    password = models.CharField(max_length=100)
    photo = models.ImageField(upload_to=user_directory_path)

    def __str__(self):
        return self.username
