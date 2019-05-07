from django.urls import path
from djangodemo.views import LaneView

urlpatterns = [
    path('', LaneView.index, name='index'),
	path('create', LaneView.get, name='create'),
	path('get/<int:laneId>/', LaneView.get, name='get'),
	path('save', LaneView.save, name='save'),
	path('getAll', LaneView.getAll, name='getAll'),
	path('delete/<int:laneId>/', LaneView.delete, name='delete'),
]
