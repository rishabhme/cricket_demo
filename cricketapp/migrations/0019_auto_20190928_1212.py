# Generated by Django 2.0.5 on 2019-09-28 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cricketapp', '0018_auto_20190928_1140'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='match',
            options={},
        ),
        migrations.AlterModelTable(
            name='club',
            table='club',
        ),
        migrations.AlterModelTable(
            name='inning',
            table='inning',
        ),
        migrations.AlterModelTable(
            name='match',
            table='match',
        ),
        migrations.AlterModelTable(
            name='player',
            table='player',
        ),
        migrations.AlterModelTable(
            name='team',
            table='team',
        ),
    ]