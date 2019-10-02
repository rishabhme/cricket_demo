# Generated by Django 2.0.5 on 2019-09-25 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cricketapp', '0011_auto_20190925_1051'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='batperformance',
            name='bat_out_bowler',
        ),
        migrations.RemoveField(
            model_name='batperformance',
            name='bat_out_fielder',
        ),
        migrations.RemoveField(
            model_name='batperformance',
            name='match',
        ),
        migrations.RemoveField(
            model_name='batperformance',
            name='player',
        ),
        migrations.RemoveField(
            model_name='bowlperformance',
            name='match',
        ),
        migrations.RemoveField(
            model_name='bowlperformance',
            name='player',
        ),
        migrations.RemoveField(
            model_name='fieldperformance',
            name='match',
        ),
        migrations.RemoveField(
            model_name='fieldperformance',
            name='player',
        ),
        migrations.RemoveField(
            model_name='performance',
            name='match',
        ),
        migrations.RemoveField(
            model_name='performance',
            name='player',
        ),
        migrations.RenameField(
            model_name='inning',
            old_name='extras_byes',
            new_name='point',
        ),
        migrations.RenameField(
            model_name='inning',
            old_name='extras_leg_byes',
            new_name='wicket',
        ),
        migrations.RemoveField(
            model_name='inning',
            name='bat_team',
        ),
        migrations.RemoveField(
            model_name='inning',
            name='bowl_team',
        ),
        migrations.RemoveField(
            model_name='inning',
            name='complete_innings',
        ),
        migrations.RemoveField(
            model_name='inning',
            name='declared',
        ),
        migrations.RemoveField(
            model_name='inning',
            name='extras_no_balls',
        ),
        migrations.RemoveField(
            model_name='inning',
            name='extras_penalties',
        ),
        migrations.RemoveField(
            model_name='inning',
            name='extras_total',
        ),
        migrations.RemoveField(
            model_name='inning',
            name='extras_wides',
        ),
        migrations.RemoveField(
            model_name='inning',
            name='overs',
        ),
        migrations.RemoveField(
            model_name='inning',
            name='wickets',
        ),
        migrations.AddField(
            model_name='inning',
            name='over',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='inning',
            name='status',
            field=models.CharField(blank=True, choices=[('won', 'Won'), ('loss', 'Loss'), ('draw', 'Draw')], max_length=10),
        ),
        migrations.AddField(
            model_name='inning',
            name='team',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='score_card_team', to='cricketapp.Team'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='inning',
            name='match',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='score_card_match', to='cricketapp.Match'),
        ),
        migrations.AlterField(
            model_name='inning',
            name='runs',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='BatPerformance',
        ),
        migrations.DeleteModel(
            name='BowlPerformance',
        ),
        migrations.DeleteModel(
            name='FieldPerformance',
        ),
        migrations.DeleteModel(
            name='Performance',
        ),
    ]
