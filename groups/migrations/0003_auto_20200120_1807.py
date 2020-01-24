# Generated by Django 3.0.2 on 2020-01-20 18:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('groups', '0002_auto_20200120_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='group_members',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
