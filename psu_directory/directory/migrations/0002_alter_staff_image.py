# Generated by Django 4.2.6 on 2023-10-24 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='image',
            field=models.ImageField(upload_to='pics'),
        ),
    ]