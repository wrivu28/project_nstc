# Generated by Django 2.1 on 2019-09-08 08:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0010_teacher_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='image',
        ),
    ]