# Generated by Django 3.0.7 on 2021-10-24 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0020_auto_20211024_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case2',
            name='client_ide',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]
