# Generated by Django 2.2 on 2018-12-13 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0009_auto_20181213_1601'),
    ]

    operations = [
        migrations.AddField(
            model_name='classroom',
            name='dayofweek',
            field=models.IntegerField(default=4),
        ),
        migrations.AlterField(
            model_name='classroom',
            name='date',
            field=models.CharField(default='2018-12-13', max_length=20),
        ),
    ]
