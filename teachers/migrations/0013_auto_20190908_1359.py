# Generated by Django 2.1 on 2019-09-08 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0012_teacher_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pic/'),
        ),
    ]