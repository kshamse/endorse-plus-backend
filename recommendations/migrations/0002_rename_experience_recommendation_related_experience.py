# Generated by Django 3.2.19 on 2023-05-27 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommendations', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recommendation',
            old_name='experience',
            new_name='related_experience',
        ),
    ]