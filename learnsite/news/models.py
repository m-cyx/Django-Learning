from distutils.command.upload import upload
from email import contentmanager
from email.mime import image
from pyexpat import model
from tabnanny import verbose
from turtle import title
from unicodedata import category
from django.db import models

# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Cодержание')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='Дата редактирования')
    image = models.ImageField(upload_to='photos/%Y/%m/d%/', blank='True')
    is_published = models.BooleanField(
        default=True, verbose_name='Опубликовано')
    category = models.ForeignKey(
        'Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(
        max_length=150, db_index=True, verbose_name='Наименование')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']
