# Generated by Django 4.1.7 on 2023-06-25 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classslot',
            name='classroom',
        ),
        migrations.RemoveField(
            model_name='faculty',
            name='user',
        ),
        migrations.RemoveField(
            model_name='section',
            name='classroom',
        ),
        migrations.RemoveField(
            model_name='section',
            name='course',
        ),
        migrations.RemoveField(
            model_name='section',
            name='faculty',
        ),
        migrations.RemoveField(
            model_name='section',
            name='time_slot',
        ),
        migrations.DeleteModel(
            name='Classroom',
        ),
        migrations.DeleteModel(
            name='ClassSlot',
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='Faculty',
        ),
        migrations.DeleteModel(
            name='Section',
        ),
    ]