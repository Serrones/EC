# Generated by Django 2.0 on 2017-12-24 04:04

from django.utils import timezone
from django.db import migrations
from ecweb.models import BasicUser

def create_superuser(apps, schema_editor):
    superuser = BasicUser()
    superuser.is_active = True
    superuser.is_superuser = True
    superuser.is_staff = True
    superuser.date_joined = timezone.now()
    superuser.username = 'admin'
    superuser.email = 'admin@admin.com'
    superuser.set_password('admin123')
    superuser.save()


class Migration(migrations.Migration):
    dependencies = [
        ('ecweb', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_superuser)
    ]