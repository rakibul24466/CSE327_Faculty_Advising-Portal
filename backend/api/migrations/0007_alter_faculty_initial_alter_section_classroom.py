# Generated by Django 4.1.7 on 2023-06-24 20:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_remove_classroom_available'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='initial',
            field=models.CharField(max_length=50, unique=True, verbose_name='Short initial  '),
        ),
        migrations.AlterField(
            model_name='section',
            name='classroom',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='api.classroom', verbose_name='Classroom'),
        ),
    ]
