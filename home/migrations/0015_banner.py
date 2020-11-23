# Generated by Django 3.1 on 2020-08-12 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20200812_1610'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('image', models.ImageField(upload_to='media')),
                ('status', models.CharField(blank=True, choices=[('active', 'active'), ('', 'default')], max_length=100)),
                ('upper_part', models.CharField(blank=True, max_length=400)),
                ('middle_part', models.CharField(blank=True, max_length=400)),
                ('lower_part', models.CharField(blank=True, max_length=400)),
                ('cross_part', models.CharField(blank=True, max_length=400)),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.category')),
            ],
        ),
    ]