# Generated by Django 4.0.10 on 2024-02-02 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('service', models.CharField(choices=[('Pedicure', 'Pedicure'), ('Manicure', 'Manicure'), ('Make Up', 'Make Up'), ('Other', 'Other')], max_length=20)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]