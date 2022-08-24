# Generated by Django 4.1 on 2022-08-23 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=30, unique=True, verbose_name='email')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('name', models.CharField(max_length=30)),
                ('is_mentor', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]