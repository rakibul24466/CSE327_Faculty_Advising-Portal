# Generated by Django 4.1.7 on 2023-06-24 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_faculty_initial_alter_section_classroom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='faculty',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='api.faculty', verbose_name='Faculty taking the class'),
        ),
    ]
