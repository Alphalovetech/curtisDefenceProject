# Generated by Django 4.2 on 2023-07-06 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polling_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='voters',
            name='email',
            field=models.EmailField(max_length=20, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='voters',
            name='image',
            field=models.ImageField(null=True, unique=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='voters',
            name='phone_number',
            field=models.CharField(max_length=9, null=True, unique=True),
        ),
    ]
