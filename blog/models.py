from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Post(models.Model):
    title = models.CharField(max_length=140)
    #body = models.TextField()
    body = RichTextUploadingField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title
