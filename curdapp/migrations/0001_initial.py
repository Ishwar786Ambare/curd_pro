# Generated by Django 3.0.6 on 2020-05-29 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_roll_no', models.ImageField(unique=True, upload_to='')),
                ('student_first_name', models.CharField(max_length=100)),
                ('student_last_name', models.CharField(max_length=100)),
            ],
        ),
    ]
