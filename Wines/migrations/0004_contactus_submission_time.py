# Generated by Django 4.2.4 on 2023-10-02 17:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Wines', '0003_contactus'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='submission_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
