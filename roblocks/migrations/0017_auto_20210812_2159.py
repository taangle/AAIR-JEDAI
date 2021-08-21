# Generated by Django 3.2.5 on 2021-08-12 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roblocks', '0016_delete_savethefiles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ebooksmodel',
            name='domain',
            field=models.FilePathField(allow_files=False, allow_folders=True, blank=True, null=True, path='./modules'),
        ),
        migrations.AlterField(
            model_name='ebooksmodel',
            name='problem',
            field=models.FilePathField(allow_files=False, allow_folders=True, blank=True, match='problem', null=True, path='./modules', recursive=True),
        ),
    ]