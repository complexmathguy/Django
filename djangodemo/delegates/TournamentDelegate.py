from django.core import exceptions
from django.core import serializers
from django.db import models
from django.db import utils

from djangodemo.models.Tournament import Tournament
from djangodemo.models.Matchup import Matchup
from djangodemo.exceptions import Exceptions

 #======================================================================
# 
# Encapsulates data for model Tournament
#
# @author 
#
#======================================================================

#======================================================================
# Class TournamentDelegate Declaration
#======================================================================
class TournamentDelegate :

#======================================================================
# Function Declarations
#======================================================================

	def get(self, tournamentId ):
		try:	
			tournament = Tournament.objects.filter(id=tournamentId)
			return tournament.first();
		except Tournament.DoesNotExist:
			raise ProcessingError("Tournament with id " + str(tournamentId) + " does not exist.")
		except utils.DatabaseError:
			raise StorageReadError()
		except Exception:
			raise GeneralError(errMsg) 

	def createFromJson(self, tournament):
		for model in serializers.deserialize("json", tournament):
			model.save()
			return model;

	def create(self, tournament):
		tournament.save()
		return tournament;

	def saveFromJson(self, tournament):
		for model in serializers.deserialize("json", tournament):
			model.save()
			return tournament;
	
	def save(self, tournament):
		tournament.save()
		return tournament;
	
	def delete(self, tournamentId ):
		errMsg = "Failed to delete Tournament from db using id " + str(tournamentId)
		
		try:
			tournament = Tournament.objects.get(id=tournamentId)
			tournament.delete()
			return True
		except Tournament.DoesNotExist:
			raise ProcessingError("Tournament with id " + str(tournamentId) + " does not exist.")
		except utils.DatabaseError:
			raise StorageReadError()
		except Exception:
			raise GeneralError(errMsg) 
	
	def getAll(self):
		try:
			all = Tournament.objects.all()
			return all;
		except utils.DatabaseError:
			raise StorageReadError("Failed to get all Tournament from db")
		except Exception:
			return None;
		
