# Generated by Django 3.1.1 on 2020-10-04 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0002_auto_20201004_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, height_field=models.IntegerField(default=0), null=True, upload_to='', width_field=models.IntegerField(default=0)),
        ),
    ]
