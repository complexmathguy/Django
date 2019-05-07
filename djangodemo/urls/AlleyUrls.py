from django.urls import path
from djangodemo.views import AlleyView

urlpatterns = [
    path('', AlleyView.index, name='index'),
	path('create', AlleyView.get, name='create'),
	path('get/<int:alleyId>/', AlleyView.get, name='get'),
	path('save', AlleyView.save, name='save'),
	path('getAll', AlleyView.getAll, name='getAll'),
	path('delete/<int:alleyId>/', AlleyView.delete, name='delete'),
]
