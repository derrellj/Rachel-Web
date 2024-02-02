# Generated by Django 4.0.10 on 2024-02-02 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('about', models.TextField()),
                ('image', models.ImageField(upload_to='uploads')),
            ],
        ),
    ]
