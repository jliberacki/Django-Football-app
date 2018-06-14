from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^details/(?P<squad_id>\w{0,50})/$', views.details),
    url(r'^player_details/(?P<player_id>\w{0,50})/$', views.player_details),
    url(r'^add_squad', views.add_squad, name="add_squad"),
    url(r'^add_player/(?P<squad_id>\w{0,50})/$', views.add_player,name="add_player"),
    url(r'^add_match', views.add_match, name="add_match")
]