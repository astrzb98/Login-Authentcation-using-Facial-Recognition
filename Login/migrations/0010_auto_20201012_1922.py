# Generated by Django 3.1.1 on 2020-10-12 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0009_auto_20201006_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(upload_to='profiles/<django.db.models.fields.CharField>'),
        ),
    ]
