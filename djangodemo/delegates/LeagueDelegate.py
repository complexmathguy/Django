from django.core import exceptions
from django.core import serializers
from django.db import models
from django.db import utils

from djangodemo.models.League import League
from djangodemo.models.Player import Player
from djangodemo.exceptions import Exceptions

 #======================================================================
# 
# Encapsulates data for model League
#
# @author 
#
#======================================================================

#======================================================================
# Class LeagueDelegate Declaration
#======================================================================
class LeagueDelegate :

#======================================================================
# Function Declarations
#======================================================================

	def get(self, leagueId ):
		try:	
			league = League.objects.filter(id=leagueId)
			return league.first();
		except League.DoesNotExist:
			raise ProcessingError("League with id " + str(leagueId) + " does not exist.")
		except utils.DatabaseError:
			raise StorageReadError()
		except Exception:
			raise GeneralError(errMsg) 

	def createFromJson(self, league):
		for model in serializers.deserialize("json", league):
			model.save()
			return model;

	def create(self, league):
		league.save()
		return league;

	def saveFromJson(self, league):
		for model in serializers.deserialize("json", league):
			model.save()
			return league;
	
	def save(self, league):
		league.save()
		return league;
	
	def delete(self, leagueId ):
		errMsg = "Failed to delete League from db using id " + str(leagueId)
		
		try:
			league = League.objects.get(id=leagueId)
			league.delete()
			return True
		except League.DoesNotExist:
			raise ProcessingError("League with id " + str(leagueId) + " does not exist.")
		except utils.DatabaseError:
			raise StorageReadError()
		except Exception:
			raise GeneralError(errMsg) 
	
	def getAll(self):
		try:
			all = League.objects.all()
			return all;
		except utils.DatabaseError:
			raise StorageReadError("Failed to get all League from db")
		except Exception:
			return None;
		
