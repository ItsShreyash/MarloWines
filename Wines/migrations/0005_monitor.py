# Generated by Django 4.2.4 on 2023-10-04 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Wines', '0004_contactus_submission_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Monitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('Login_time', models.DateTimeField(auto_now_add=True)),
                ('Logout_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
