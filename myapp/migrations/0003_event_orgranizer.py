# Generated by Django 4.2.4 on 2023-08-06 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_remove_event_id_event_event_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='orgranizer',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]