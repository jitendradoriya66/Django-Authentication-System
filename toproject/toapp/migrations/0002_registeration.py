# Generated by Django 5.0.2 on 2025-02-24 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='registeration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=128)),
                ('c_password', models.CharField(max_length=128)),
            ],
        ),
    ]
