# Generated by Django 2.0.5 on 2019-09-25 05:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cricketapp', '0002_auto_20190925_0505'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='match',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
