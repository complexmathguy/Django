from django.urls import path
from djangodemo.views import TournamentView

urlpatterns = [
    path('', TournamentView.index, name='index'),
	path('create', TournamentView.get, name='create'),
	path('get/<int:tournamentId>/', TournamentView.get, name='get'),
	path('save', TournamentView.save, name='save'),
	path('getAll', TournamentView.getAll, name='getAll'),
	path('delete/<int:tournamentId>/', TournamentView.delete, name='delete'),
]
