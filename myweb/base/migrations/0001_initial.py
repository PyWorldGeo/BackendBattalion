# Generated by Django 5.0.6 on 2024-06-20 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
                ('picture', models.CharField(max_length=300)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=500)),
                ('content', models.CharField(max_length=200)),
            ],
        ),
    ]
