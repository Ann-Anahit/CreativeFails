# Generated by Django 5.0.7 on 2024-12-11 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customuser_is_artist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_artist',
            field=models.BooleanField(default=False),
        ),
    ]
