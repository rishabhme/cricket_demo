# Generated by Django 2.0.5 on 2019-09-30 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cricketapp', '0020_player_is_delete'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
