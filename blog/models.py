from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    header_image=models.ImageField(blank=True,null=True, upload_to="images/")
    text = RichTextUploadingField(blank=True,null=True)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
 
    def publish(self):
        self.published_date = timezone.now()
        self.save()
 
    def __str__(self):
        return self.title
