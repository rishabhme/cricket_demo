# Generated by Django 2.0.5 on 2019-09-25 05:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cricketapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='game_type',
        ),
        migrations.RemoveField(
            model_name='match',
            name='last_updated',
        ),
        migrations.RemoveField(
            model_name='match',
            name='match_notes',
        ),
        migrations.RemoveField(
            model_name='match',
            name='match_type',
        ),
        migrations.RemoveField(
            model_name='match',
            name='processing_issue',
        ),
        migrations.RemoveField(
            model_name='match',
            name='result_applied_to',
        ),
        migrations.RemoveField(
            model_name='match',
            name='result_description',
        ),
        migrations.RemoveField(
            model_name='match',
            name='status',
        ),
        migrations.RemoveField(
            model_name='match',
            name='toss',
        ),
    ]
