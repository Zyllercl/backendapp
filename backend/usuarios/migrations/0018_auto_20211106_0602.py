# Generated by Django 3.0.7 on 2021-11-06 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0017_auto_20211106_0546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='files',
            field=models.FileField(upload_to='documents/cases/', verbose_name='Archivos'),
        ),
    ]
