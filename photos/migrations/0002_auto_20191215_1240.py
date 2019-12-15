# Generated by Django 2.2.6 on 2019-12-15 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('photos', '0001_initial'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meme',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.Profile'),
        ),
        migrations.AddField(
            model_name='meme',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='memes', to='photos.Tag'),
        ),
    ]
