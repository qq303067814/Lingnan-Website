# Generated by Django 2.2 on 2018-12-22 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rewardu', '0005_resultu_uname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resultu',
            name='task',
        ),
        migrations.RemoveField(
            model_name='resultu',
            name='user',
        ),
    ]
