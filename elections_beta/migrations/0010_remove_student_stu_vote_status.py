# Generated by Django 2.2.1 on 2019-05-25 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elections_beta', '0009_auto_20190519_2212'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='stu_vote_status',
        ),
    ]
