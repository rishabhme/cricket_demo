from django.db import models

# Create your models here.
# -*- coding: utf-8 -*-

# Django Imports
from django.db import models
from django.db.models import Sum, F, Max, Q


# 3rd Party Imports
import pytz

# Python Imports


class Club(models.Model):
    name = models.CharField(max_length=255)
    home_club = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "club"
'''Team Model'''
'''Used to store information about each Team'''
'''Dependency on Club '''
class Team(models.Model):
    club = models.ForeignKey('Club', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default='unsure')
    logo = models.ImageField(upload_to='image_logo/', blank=False)
    def __str__(self):
        return str(self.club) + ' - ' + self.name

    class Meta:
        db_table = "team"

'''Player Model'''
'''Used to store information about each player'''
class Player(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    image_uri = models.ImageField(upload_to='image_user/', blank=False)
    player_jersey_number = models.CharField(max_length=255)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return str(self.team) + ': ' + self.first_name

    class Meta:
        db_table = "player"

'''Match model.'''
'''Used for storing data about matches'''
'''Dependency on Team'''
class Match(models.Model):
    class Meta:
        verbose_name_plural = "matches"
    match_date = models.DateTimeField()
    team_1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_team')
    team_2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_team')
    winner = models.CharField(max_length=25,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.match_date)

    class Meta:
        db_table = "match"

'''Match player detail model.'''
'''Used for storing data about player details playing the match'''
'''Dependency on  Match Team Player'''
class MatchPlayerDetails(models.Model):
    match_id = models.ForeignKey(Match, related_name="match_player", blank=False, on_delete=models.CASCADE)
    team_id = models.ForeignKey(Team, related_name="match_team", blank=False, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, related_name="user_player", blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.match_id)

    class Meta:
        db_table = "match_player_detail"

'''Inning Model'''
'''Used for storing information about each inning in a match.'''
'''Dependency on matchplayerdetails'''
class Inning(models.Model):
    SCORE_STATUS_CHOICE = (
        ('won', 'Won'),
        ('loss', 'Loss'),
        ('draw', 'Draw'),
    )

    match_player = models.ForeignKey(MatchPlayerDetails, related_name="match_player_detail", blank=False, on_delete=models.CASCADE)
    runs = models.IntegerField(blank=False, default=0)
    wicket = models.IntegerField(blank=False, default=0)
    over = models.FloatField(blank=False, default=0.0)
    status = models.CharField(max_length=10, choices=SCORE_STATUS_CHOICE, blank=True)
    inning_no = models.IntegerField(default=0)


    def __str__(self):
        return str(self.match_player.team_id)

    class Meta:
        db_table = "inning"

'''playerScoreCard'''
'''Used for storing information about player each inning.'''
'''Dependency on inning and player'''
class PlayerScoreCard(models.Model):
    PLAYER_STATUS_CHOICE = (
        ('out', 'Out'),
        ('notout', 'Not Out'),
        ('notplayed', 'Not Played'),
    )

    inning = models.ForeignKey(Inning, related_name="player_inning", blank=False, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, related_name="player_score", blank=False, on_delete=models.CASCADE)
    runs = models.CharField(max_length=10,blank=True, default=0)
    fifty = models.CharField(max_length=10,blank=True, default=0)
    hundred = models.CharField(max_length=10,blank=True, default=0)
    fours = models.CharField(max_length=10,blank=True, default=0)
    sixes = models.CharField(max_length=10,blank=True, default=0)
    status = models.CharField(max_length=10, choices = PLAYER_STATUS_CHOICE, blank=True)

    def __str__(self):
        return self.player.first_name

    class Meta:
        db_table = "score_card_player"




