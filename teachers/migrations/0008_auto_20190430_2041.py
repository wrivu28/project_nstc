# Generated by Django 2.1.5 on 2019-04-30 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0007_auto_20190105_2228'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='stream',
            new_name='dept',
        ),
    ]
