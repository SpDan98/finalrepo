# Generated by Django 4.2.1 on 2023-06-06 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articleapp', '0003_articlesblock'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='published',
            field=models.BooleanField(default=False),
        ),
    ]