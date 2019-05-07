import json

from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse

from djangodemo.delegates.AlleyDelegate import AlleyDelegate

 #======================================================================
# 
# Encapsulates data for View Alley
#
# @author 
#
#======================================================================

#======================================================================
# Class AlleyView function declarations
#======================================================================
def index(request):
	return HttpResponse("Hello, world. You're at the Alley index.")

def get(request, alleyId ):
	delegate = AlleyDelegate()
	responseData = delegate.get( alleyId )
	asJson = serializers.serialize("json", responseData)
	return HttpResponse(asJson, content_type="application/json");

def create(request):
	alley = json.loads(request.body)
	delegate = AlleyDelegate()
	responseData = delegate.createFromJson( alley )
	asJson = serializers.serialize("json", responseData)
	return HttpResponse(asJson, content_type="application/json");

def save(request):
	alley = json.loads(request.body)
	delegate = AlleyDelegate()
	responseData = delegate.save( alley )
	asJson = serializers.serialize("json", responseData)
	return HttpResponse(asJson, content_type="application/json");

def delete(request, alleyId ):
	delegate = AlleyDelegate()
	responseData = delegate.delete( alleyId )
	return HttpResponse(responseData, content_type="application/json");

def getAll(request):
	delegate = AlleyDelegate()
	responseData = delegate.getAll()
	asJson = serializers.serialize("json", responseData)
	return HttpResponse(asJson, content_type="application/json");

