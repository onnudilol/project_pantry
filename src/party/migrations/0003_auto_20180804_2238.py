# Generated by Django 2.0.7 on 2018-08-04 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('party', '0002_auto_20180804_2223'),
    ]

    operations = [
        migrations.AddField(
            model_name='party',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='party',
            name='title',
            field=models.CharField(default='', max_length=300),
            preserve_default=False,
        ),
    ]
