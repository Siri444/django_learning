# Generated by Django 5.0.6 on 2024-07-20 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0002_alter_drinks_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('roll', models.IntegerField()),
                ('city', models.CharField(max_length=50)),
            ],
        ),
    ]
