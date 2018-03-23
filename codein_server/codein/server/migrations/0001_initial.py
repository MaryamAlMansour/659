# Generated by Django 2.0.2 on 2018-03-14 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=12)),
                ('password', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=40)),
                ('developer', models.BooleanField(default=False)),
                ('python', models.BooleanField(default=False)),
                ('java', models.BooleanField(default=False)),
                ('standard_c', models.BooleanField(default=False)),
                ('c_plus_plus', models.BooleanField(default=False)),
                ('other_language', models.CharField(max_length=12)),
            ],
        ),
    ]
