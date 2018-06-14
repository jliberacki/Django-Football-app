# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect

from .models import Squad, Player, Match

def index(request):
    squads = Squad.objects.all()[:10]
    matches = Match.objects.all()[:10]

    context = {
        'squads': squads,
        'matches': matches
    }
    return render(request, 'index.html',context)

def details(request, squad_id):
    squad = Squad.objects.get(id=squad_id)
    players = Player.objects.all()

    players = players.filter(squad=squad)

    context = {
        'squad': squad,
        'players': players
    }
    return render(request, 'details.html',context)

def player_details(request, player_id):
    player = Player.objects.get(id=player_id)

    context = {
        'player': player,
    }

    if(request.method == 'POST'):
        squad_id = str(player.squad.id)
        player.delete()
        return redirect('/squads/details/'+squad_id)
    else: 
        return render(request, 'player_details.html',context)

def add_squad(request):
    if(request.method == 'POST'):
        name = request.POST['name']
        informations = request.POST['text']
        squad = Squad(name=name,informations=informations)
        squad.save()
        return redirect('/squads')
    else:
        return render(request, 'add_squad.html')

def add_player(request,squad_id):
    if(request.method == 'POST'):
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        num = request.POST['num']
        pos = request.POST['pos']
        squad = Squad.objects.get(id=squad_id)
        player = Player(first_name=first_name,last_name=last_name,number=num,position=pos,squad=squad)
        player.save()
        return redirect('/squads/details/'+squad_id)
    else:
        return render(request, 'add_player.html')

def add_match(request):
    if(request.method == 'POST'):
        home_name = request.POST['hname']
        away_name = request.POST['aname']
        result = request.POST['res']
        if not Squad.objects.filter(name=home_name).exists():
            messages.info(request, 'Please type existing home team')
            return HttpResponseRedirect('/squads/add_match')
        elif not Squad.objects.filter(name=away_name).exists():
            messages.info(request, 'Please type existing away team')
            return HttpResponseRedirect('/squads/add_match')  
        else:
            home_team = Squad.objects.get(name=home_name)
            away_team = Squad.objects.get(name=away_name)
            match = Match(home_team=home_team,away_team=away_team, result=result)
            match.save()
            return redirect('/squads')
    else:
        return render(request, 'add_match.html')