# Generated by Django 2.2 on 2018-12-06 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_auto_20181206_0945'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='submittime',
            field=models.CharField(default='None', max_length=10),
        ),
    ]
