# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Squad(models.Model):
    name = models.CharField(max_length=30)
    informations = models.TextField()
    def __str__(self):
        return self.name

class Player(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    number = models.CharField(max_length=2)
    position = models.CharField(max_length=20)
    squad = models.ForeignKey(Squad)
    def __str__(self):
        return self.first_name +' '+ self.last_name

class Match(models.Model):
    home_team = models.ForeignKey(Squad, related_name='home_team')
    away_team = models.ForeignKey(Squad, related_name='away_team')
    result = models.CharField(max_length=5)
    def __str__(self):
        return self.home_team.name +' - '+ self.away_team.name
    