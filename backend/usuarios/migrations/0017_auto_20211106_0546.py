# Generated by Django 3.0.7 on 2021-11-06 05:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0016_auto_20211106_0543'),
    ]

    operations = [
        migrations.RenameField(
            model_name='case',
            old_name='client',
            new_name='case_client',
        ),
        migrations.RenameField(
            model_name='case',
            old_name='teacher',
            new_name='case_teacher',
        ),
    ]
