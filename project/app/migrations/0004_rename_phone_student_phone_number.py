# Generated by Django 4.0.3 on 2022-08-16 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_student_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='phone',
            new_name='phone_number',
        ),
    ]