# Generated by Django 5.0.6 on 2024-07-03 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_projects_remove_about_us_project_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='about_us',
            name='project_completed',
            field=models.BigIntegerField(default=0),
        ),
    ]
