# Generated by Django 4.0.4 on 2022-05-29 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_category_title2_alter_news_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='title2',
        ),
    ]