# Generated by Django 2.1.1 on 2018-09-06 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0002_auto_20180902_1445'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='phone_no_1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='teacher',
            name='phone_no_2',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]