# Generated by Django 4.1.5 on 2023-01-23 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_project_liked_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='liked_by',
        ),
    ]
