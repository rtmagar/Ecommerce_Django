# Generated by Django 3.1 on 2020-08-12 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='s_image',
        ),
    ]
