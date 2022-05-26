from distutils.command.upload import upload
from email import contentmanager
from email.mime import image
from pyexpat import model
from turtle import title
from django.db import models

# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='photos/%Y/%m/d%/')
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title
