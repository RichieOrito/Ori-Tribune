# Generated by Django 4.0.3 on 2022-03-01 21:39

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_alter_article_post'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Editor',
        ),
        migrations.AlterField(
            model_name='article',
            name='post',
            field=tinymce.models.HTMLField(),
        ),
    ]
