# Generated by Django 2.0.7 on 2018-08-04 22:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('party', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='party',
            old_name='availability',
            new_name='dictator',
        ),
        migrations.RemoveField(
            model_name='foodlist',
            name='price_max',
        ),
        migrations.AlterField(
            model_name='foodlist',
            name='party',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='party.Party'),
        ),
    ]
