# Generated by Django 4.0.2 on 2022-02-23 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_article_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_image',
            field=models.ImageField(upload_to='articles/'),
        ),
    ]