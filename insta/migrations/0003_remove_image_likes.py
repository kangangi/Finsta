# Generated by Django 3.0.6 on 2020-05-31 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0002_auto_20200529_2106'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='likes',
        ),
    ]
