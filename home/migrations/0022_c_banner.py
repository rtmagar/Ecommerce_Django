# Generated by Django 3.1 on 2020-08-15 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_banner'),
    ]

    operations = [
        migrations.CreateModel(
            name='C_Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('image', models.TextField()),
                ('discount', models.CharField(blank=True, max_length=400)),
            ],
        ),
    ]