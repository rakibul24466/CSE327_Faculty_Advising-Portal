# Generated by Django 4.2.1 on 2023-06-24 18:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_classroom_available'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classroom',
            name='available',
        ),
    ]
