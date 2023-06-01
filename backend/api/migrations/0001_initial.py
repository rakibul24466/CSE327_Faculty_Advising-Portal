# Generated by Django 4.1.7 on 2023-06-01 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('building', models.CharField(max_length=5, verbose_name='academic building abbbrebiation')),
                ('roomNo', models.PositiveIntegerField(primary_key=True, serialize=False, verbose_name='classroom number')),
                ('seat', models.PositiveIntegerField(verbose_name='Available seat for students')),
                ('details', models.CharField(max_length=150, verbose_name='Classroom details e.g. projector,computer et')),
            ],
            options={
                'verbose_name': 'Classroom',
                'verbose_name_plural': 'Classrooms',
            },
        ),
        migrations.CreateModel(
            name='ClassSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available', models.BooleanField(default=True, verbose_name='Class Slot available or not')),
                ('slot', models.IntegerField(choices=[(1, 'S - 08:00 AM - 09:00 AM'), (2, 'S - 09:10 AM - 10:10 AM'), (3, 'S - 10:20 AM - 11:20 AM'), (4, 'S - 11:30 AM - 12:30 PM'), (5, 'S - 12:40 PM - 01:40 PM'), (6, 'S - 01:50 PM - 02:50 PM'), (7, 'S - 03:00 PM - 04:00 PM'), (8, 'S - 04:10 PM - 05:10 PM'), (9, 'S - 05:20 PM - 06:20 PM'), (10, 'T - 08:00 AM - 09:00 AM'), (11, 'T - 09:10 AM - 10:10 AM'), (12, 'T - 10:20 AM - 11:20 AM'), (13, 'T - 11:30 AM - 12:30 PM'), (14, 'T - 12:40 PM - 01:40 PM'), (15, 'T - 01:50 PM - 02:50 PM'), (16, 'T - 03:00 PM - 04:00 PM'), (17, 'T - 04:10 PM - 05:10 PM'), (18, 'T - 05:20 PM - 06:20 PM'), (19, 'R - 08:00 AM - 09:00 AM'), (20, 'R - 09:10 AM - 10:10 AM'), (21, 'R - 10:20 AM - 11:20 AM'), (22, 'R - 11:30 AM - 12:30 PM'), (23, 'R - 12:40 PM - 01:40 PM'), (24, 'R - 01:50 PM - 02:50 PM'), (25, 'R - 03:00 PM - 04:00 PM'), (26, 'R - 04:10 PM - 05:10 PM'), (27, 'R - 05:20 PM - 06:20 PM'), (28, 'A - 08:00 AM - 09:00 AM'), (29, 'A - 09:10 AM - 10:10 AM'), (30, 'A - 10:20 AM - 11:20 AM'), (31, 'A - 11:30 AM - 12:30 PM'), (32, 'A - 12:40 PM - 01:40 PM'), (33, 'A - 01:50 PM - 02:50 PM'), (34, 'A - 03:00 PM - 04:00 PM'), (35, 'A - 04:10 PM - 05:10 PM'), (36, 'A - 05:20 PM - 06:20 PM'), (37, 'M - 08:00 AM - 09:00 AM'), (38, 'M - 09:10 AM - 10:10 AM'), (39, 'M - 10:20 AM - 11:20 AM'), (40, 'M - 11:30 AM - 12:30 PM'), (41, 'M - 12:40 PM - 01:40 PM'), (42, 'M - 01:50 PM - 02:50 PM'), (43, 'M - 03:00 PM - 04:00 PM'), (44, 'M - 04:10 PM - 05:10 PM'), (45, 'M - 05:20 PM - 06:20 PM'), (46, 'W - 08:00 AM - 09:00 AM'), (47, 'W - 09:10 AM - 10:10 AM'), (48, 'W - 10:20 AM - 11:20 AM'), (49, 'W - 11:30 AM - 12:30 PM'), (50, 'W - 12:40 PM - 01:40 PM'), (51, 'W - 01:50 PM - 02:50 PM'), (52, 'W - 03:00 PM - 04:00 PM'), (53, 'W - 04:10 PM - 05:10 PM'), (54, 'W - 05:20 PM - 06:20 PM')], verbose_name='Class day - time ')),
                ('name', models.CharField(blank=True, max_length=50, verbose_name='Slot name/time')),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.classroom', verbose_name='Classs room no')),
            ],
            options={
                'verbose_name': 'ClassSlot',
                'verbose_name_plural': 'ClassSlots',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=10, verbose_name='course Code')),
                ('credit', models.FloatField(verbose_name='Course Credit')),
                ('type', models.CharField(blank=True, choices=[('', 'Theory'), ('L', 'Lab/Practical')], max_length=10, verbose_name='Course Type e.g. lab,theory ')),
                ('number_of_section', models.IntegerField(verbose_name='Total number of Section ')),
            ],
            options={
                'verbose_name': 'Course',
                'verbose_name_plural': 'Courses',
            },
        ),
        migrations.CreateModel(
            name='Educator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name ')),
                ('initial', models.CharField(max_length=50, verbose_name='Short initial  ')),
                ('designation', models.CharField(blank=True, max_length=50, verbose_name='Designation ')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Email')),
                ('ext', models.IntegerField(blank=True, default=0, verbose_name='Phone extention number')),
                ('room', models.IntegerField(blank=True, default=0, verbose_name='Room Number')),
                ('mobile', models.CharField(blank=True, max_length=50, verbose_name='Mobile Number')),
            ],
            options={
                'verbose_name': 'Person',
                'verbose_name_plural': 'Persons',
            },
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('educator_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.educator')),
                ('total_credit', models.FloatField(verbose_name='Number of credit taken')),
            ],
            options={
                'verbose_name': 'Faculty',
                'verbose_name_plural': 'Faculties',
            },
            bases=('api.educator',),
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.IntegerField(verbose_name='Section no')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.course', verbose_name='Course Name')),
            ],
            options={
                'verbose_name': 'Section',
                'verbose_name_plural': 'Sections',
            },
        ),
        migrations.CreateModel(
            name='CourseTaken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_slot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.classslot', verbose_name='Class Time')),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.classroom', verbose_name='Classroom')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.course', verbose_name='Course Section')),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.faculty', verbose_name='Faculty Name')),
            ],
            options={
                'verbose_name': 'Course_Taken',
                'verbose_name_plural': 'Course_Takens',
            },
        ),
    ]
