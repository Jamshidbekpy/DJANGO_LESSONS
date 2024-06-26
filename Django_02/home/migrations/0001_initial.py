# Generated by Django 5.0.6 on 2024-06-24 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('cart', models.ImageField(blank=True, default=None, null=True, upload_to='news/')),
                ('video', models.URLField(blank=True, null=True)),
                ('desc', models.TextField()),
                ('body', models.TextField()),
                ('category', models.ManyToManyField(to='home.newscategory')),
            ],
            options={
                'verbose_name': 'new',
                'verbose_name_plural': 'news',
            },
        ),
    ]
