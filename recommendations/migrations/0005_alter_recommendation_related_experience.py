# Generated by Django 3.2.19 on 2023-05-27 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('experiences', '0004_alter_experience_profile'),
        ('recommendations', '0004_auto_20230527_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommendation',
            name='related_experience',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recommendations', to='experiences.experience'),
        ),
    ]
