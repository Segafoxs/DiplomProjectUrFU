# Generated by Django 5.1.4 on 2024-12-19 07:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_created=True)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Worker_is_mymodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='HistoryPermit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=255)),
                ('type_of', models.CharField(choices=[('SIMPLE', 'simple'), ('LINEAR', 'linear'), ('FIRE', 'fire')], max_length=255)),
                ('number', models.CharField(max_length=255)),
                ('master_of_work', models.CharField(max_length=255)),
                ('worker', models.CharField(max_length=255)),
                ('master', models.CharField(max_length=255)),
                ('work_description', models.CharField(max_length=255)),
                ('start_of_work', models.DateTimeField(max_length=255)),
                ('end_of_work', models.DateTimeField(max_length=255)),
                ('condition', models.CharField(max_length=255)),
                ('time_of_permit', models.CharField(max_length=255, verbose_name='Наряд выдал')),
                ('signature_from_director', models.CharField(max_length=255)),
                ('signature_from_daily_manager', models.CharField(max_length=255)),
                ('create_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='TypeOfWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_created=True)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Work_is_mymodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('name', models.CharField(max_length=100)),
                ('role', models.CharField(choices=[('DIRECTOR', 'Начальник цеха'), ('MASTER', 'MASTER'), ('WORKER', 'WORKER'), ('DAILYMANAGER', 'DAILYMANAGER'), ('STATIONENGINEER', 'STATIONENGINEER')], max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hello.department')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Director_is_mymodel',
            fields=[
                ('worker_is_mymodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hello.worker_is_mymodel')),
            ],
            bases=('hello.worker_is_mymodel',),
        ),
        migrations.CreateModel(
            name='Executor_is_mymodel',
            fields=[
                ('worker_is_mymodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hello.worker_is_mymodel')),
            ],
            bases=('hello.worker_is_mymodel',),
        ),
        migrations.CreateModel(
            name='Manager_is_mymodel',
            fields=[
                ('worker_is_mymodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hello.worker_is_mymodel')),
            ],
            bases=('hello.worker_is_mymodel',),
        ),
        migrations.CreateModel(
            name='ShiftManager_is_mymodel',
            fields=[
                ('worker_is_mymodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hello.worker_is_mymodel')),
            ],
            bases=('hello.worker_is_mymodel',),
        ),
        migrations.CreateModel(
            name='Permit',
            fields=[
                ('number', models.BigAutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('approval', 'approval'), ('work', 'work'), ('closed', 'closed')], default='approval', max_length=255)),
                ('countWorker', models.CharField(max_length=255)),
                ('work_description', models.CharField(max_length=255)),
                ('start_of_work', models.DateTimeField(max_length=255)),
                ('end_of_work', models.DateTimeField(max_length=255)),
                ('condition', models.CharField(max_length=255)),
                ('daily_manager', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dailymanager', to=settings.AUTH_USER_MODEL)),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hello.department', verbose_name='Департамент')),
                ('director', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='time', to=settings.AUTH_USER_MODEL)),
                ('employ', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='employofwork', to=settings.AUTH_USER_MODEL)),
                ('executor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='executorofwork', to=settings.AUTH_USER_MODEL)),
                ('master_of_work', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='masterofwork', to=settings.AUTH_USER_MODEL)),
                ('station_engineer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='statengineer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]