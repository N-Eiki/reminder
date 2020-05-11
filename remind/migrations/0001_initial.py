# Generated by Django 3.0.3 on 2020-05-11 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SubjectModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('weekday', models.CharField(max_length=3)),
                ('timetable', models.IntegerField()),
                ('remind', models.BooleanField(default=True)),
                ('sns_id', models.CharField(max_length=100)),
                ('remind_class', models.TextField()),
                ('remind_task', models.TextField()),
            ],
        ),
    ]
