from .views import *
from django.urls import path

app_name = 'cricketapp'
urlpatterns = [
	path('', DashboardView.as_view(), name='dashboard'),
	path('add/match/', MatchView.as_view(), name='add-match'),
	path('player/detail/<int:pk>/', PlayerDetailView.as_view(), name='player-detail'),
	path('player/detail/<int:pk>/', PlayerDetailView.as_view(), name='player-detail'),
	path('add/team/', AddTeamView.as_view(), name='add-team'),
	path('score/', MatchScoreView.as_view(), name='score'),
	path('ajax_team_list/', AjaxTeamListView.as_view(), name='ajax_team_list'),
	path('player-list/<int:pk>/', PlayerListView.as_view(), name='player-list'),
	path('player/<int:pk>/', AddPlayerView.as_view(), name='player'),
	path('player/delete/<int:pk>/', DeletePlayerView.as_view(), name='player-delete'),

]