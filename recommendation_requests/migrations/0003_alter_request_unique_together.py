# Generated by Django 3.2.19 on 2023-07-02 22:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation_requests', '0002_auto_20230527_1109'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='request',
            unique_together=set(),
        ),
    ]