# Generated by Django 2.2.6 on 2019-12-15 12:40

from django.db import migrations, models
import uuid
import versatileimagefield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meme',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('image', versatileimagefield.fields.VersatileImageField(upload_to='meme')),
                ('ppoi', versatileimagefield.fields.PPOIField(default='0.5x0.5', editable=False, max_length=20)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Meme',
                'verbose_name_plural': 'Memes',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('tag', models.TextField(default='#DankMeme')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
