# Generated by Django 4.2.4 on 2023-08-11 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='post_images'),
        ),
    ]
