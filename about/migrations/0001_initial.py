# Generated by Django 4.0.10 on 2024-02-02 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('file', models.FileField(blank=True, upload_to='files/')),
                ('image', models.ImageField(blank=True, upload_to='uploads/')),
            ],
        ),
    ]