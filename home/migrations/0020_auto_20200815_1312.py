# Generated by Django 3.1 on 2020-08-15 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_auto_20200814_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.TextField(),
        ),
    ]