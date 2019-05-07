import json

from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse

from djangodemo.delegates.LaneDelegate import LaneDelegate

 #======================================================================
# 
# Encapsulates data for View Lane
#
# @author 
#
#======================================================================

#======================================================================
# Class LaneView function declarations
#======================================================================
def index(request):
	return HttpResponse("Hello, world. You're at the Lane index.")

def get(request, laneId ):
	delegate = LaneDelegate()
	responseData = delegate.get( laneId )
	asJson = serializers.serialize("json", responseData)
	return HttpResponse(asJson, content_type="application/json");

def create(request):
	lane = json.loads(request.body)
	delegate = LaneDelegate()
	responseData = delegate.createFromJson( lane )
	asJson = serializers.serialize("json", responseData)
	return HttpResponse(asJson, content_type="application/json");

def save(request):
	lane = json.loads(request.body)
	delegate = LaneDelegate()
	responseData = delegate.save( lane )
	asJson = serializers.serialize("json", responseData)
	return HttpResponse(asJson, content_type="application/json");

def delete(request, laneId ):
	delegate = LaneDelegate()
	responseData = delegate.delete( laneId )
	return HttpResponse(responseData, content_type="application/json");

def getAll(request):
	delegate = LaneDelegate()
	responseData = delegate.getAll()
	asJson = serializers.serialize("json", responseData)
	return HttpResponse(asJson, content_type="application/json");

