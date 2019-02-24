# Generated by Django 2.0.10 on 2019-02-24 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.IntegerField(choices=[(1, 'student'), (2, 'advisor'), (3, 'approver'), (4, 'mentor')], default=1),
        ),
    ]