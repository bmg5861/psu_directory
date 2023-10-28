# Generated by Django 4.2.6 on 2023-10-24 01:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('discription', models.TextField(max_length=250)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]