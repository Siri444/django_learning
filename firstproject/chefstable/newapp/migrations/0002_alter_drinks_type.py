# Generated by Django 5.0.6 on 2024-06-30 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drinks',
            name='type',
            field=models.CharField(default='hot', max_length=50),
        ),
    ]
