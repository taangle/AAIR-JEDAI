# Generated by Django 3.1.6 on 2021-03-12 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roblocks', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ebooksmodel',
            options={},
        ),
        migrations.RemoveField(
            model_name='ebooksmodel',
            name='pdf',
        ),
        migrations.RemoveField(
            model_name='ebooksmodel',
            name='title',
        ),
        migrations.AddField(
            model_name='ebooksmodel',
            name='docs',
            field=models.FileField(blank=True, null=True, upload_to='documents/'),
        ),
    ]