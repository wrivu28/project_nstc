# Generated by Django 2.1.1 on 2018-09-23 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0006_auto_20180916_1930'),
    ]

    operations = [
        migrations.RenameField(
            model_name='formfills',
            old_name='is_gen_deatils_filled',
            new_name='is_gen_details_filled',
        ),
        migrations.AddField(
            model_name='details',
            name='guardian_mobile_no',
            field=models.IntegerField(default='000'),
        ),
    ]
