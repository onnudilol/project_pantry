# Generated by Django 2.1 on 2018-09-04 01:12

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('party', '0005_auto_20180904_0100'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='party',
            name='user',
        ),
        migrations.AddField(
            model_name='party',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
