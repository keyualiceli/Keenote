# Generated by Django 3.0.7 on 2020-07-10 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_skill'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='reflections',
            field=models.TextField(default='Learning feels good!'),
        ),
    ]
