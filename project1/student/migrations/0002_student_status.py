# Generated by Django 4.0.4 on 2022-05-03 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
