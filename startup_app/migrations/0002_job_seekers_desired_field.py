# Generated by Django 3.0.3 on 2020-02-23 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startup_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job_seekers',
            name='desired_field',
            field=models.CharField(default='NULL', max_length=1000),
        ),
    ]
