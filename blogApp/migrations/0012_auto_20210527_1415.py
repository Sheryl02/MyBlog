# Generated by Django 3.1.7 on 2021-05-27 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0011_auto_20210527_0054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(related_name='cats', to='blogApp.Category'),
        ),
    ]
