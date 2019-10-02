# Generated by Django 2.0.5 on 2019-09-25 07:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cricketapp', '0007_match_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inning',
            name='highlights',
        ),
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cricketapp.Team'),
            preserve_default=False,
        ),
    ]
