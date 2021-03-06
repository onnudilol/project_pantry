# Generated by Django 2.0.7 on 2018-08-04 22:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Allergen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
            ],
        ),
        migrations.RemoveField(
            model_name='dietaryrestriction',
            name='fish',
        ),
        migrations.RemoveField(
            model_name='dietaryrestriction',
            name='milk',
        ),
        migrations.RemoveField(
            model_name='dietaryrestriction',
            name='nuts',
        ),
        migrations.RemoveField(
            model_name='dietaryrestriction',
            name='peanuts',
        ),
        migrations.RemoveField(
            model_name='dietaryrestriction',
            name='shellfish',
        ),
        migrations.RemoveField(
            model_name='dietaryrestriction',
            name='soy',
        ),
        migrations.RemoveField(
            model_name='dietaryrestriction',
            name='tree_nuts',
        ),
        migrations.RemoveField(
            model_name='dietaryrestriction',
            name='wheat',
        ),
        migrations.AddField(
            model_name='allergen',
            name='list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_profile.DietaryRestriction'),
        ),
    ]
