# Generated by Django 4.1.7 on 2023-06-02 08:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0002_alter_educator_options_alter_coursetaken_class_slot_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='section',
            name='id',
        ),
        migrations.AddField(
            model_name='faculty',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User authenticaiton profile'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='classroom',
            name='building',
            field=models.IntegerField(choices=[(1, 'SAC'), (2, 'NAC'), (3, 'LIB'), (4, 'ADMIN')], verbose_name='academic building abbbrebiation'),
        ),
        migrations.AlterField(
            model_name='course',
            name='number_of_section',
            field=models.IntegerField(default=0, verbose_name='Total number of Section '),
        ),
        migrations.AlterField(
            model_name='section',
            name='no',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True, verbose_name='Section no'),
        ),
    ]
