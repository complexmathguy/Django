import json

from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse

from djangodemo.delegates.GameDelegate import GameDelegate

 #======================================================================
# 
# Encapsulates data for View Game
#
# @author 
#
#======================================================================

#======================================================================
# Class GameView function declarations
#======================================================================
def index(request):
	return HttpResponse("Hello, world. You're at the Game index.")

def get(request, gameId ):
	delegate = GameDelegate()
	responseData = delegate.get( gameId )
	asJson = serializers.serialize("json", responseData)
	return HttpResponse(asJson, content_type="application/json");

def create(request):
	game = json.loads(request.body)
	delegate = GameDelegate()
	responseData = delegate.createFromJson( game )
	asJson = serializers.serialize("json", responseData)
	return HttpResponse(asJson, content_type="application/json");

def save(request):
	game = json.loads(request.body)
	delegate = GameDelegate()
	responseData = delegate.save( game )
	asJson = serializers.serialize("json", responseData)
	return HttpResponse(asJson, content_type="application/json");

def delete(request, gameId ):
	delegate = GameDelegate()
	responseData = delegate.delete( gameId )
	return HttpResponse(responseData, content_type="application/json");

def getAll(request):
	delegate = GameDelegate()
	responseData = delegate.getAll()
	asJson = serializers.serialize("json", responseData)
	return HttpResponse(asJson, content_type="application/json");

