# Generated by Django 3.2.13 on 2022-06-13 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='generaluser',
            name='usertype',
            field=models.IntegerField(choices=[(1, 'ADMIN'), (2, 'USER')], default=2),
        ),
    ]
