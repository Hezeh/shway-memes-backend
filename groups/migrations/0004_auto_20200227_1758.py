# Generated by Django 3.0.3 on 2020-02-27 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0003_auto_20200226_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grouppost',
            name='post',
            field=models.ImageField(height_field='400', upload_to=''),
        ),
    ]
