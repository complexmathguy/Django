from django.urls import path
from djangodemo.views import GameView

urlpatterns = [
    path('', GameView.index, name='index'),
	path('create', GameView.get, name='create'),
	path('get/<int:gameId>/', GameView.get, name='get'),
	path('save', GameView.save, name='save'),
	path('getAll', GameView.getAll, name='getAll'),
	path('delete/<int:gameId>/', GameView.delete, name='delete'),
]
