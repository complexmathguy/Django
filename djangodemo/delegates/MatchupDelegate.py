from django.core import exceptions
from django.core import serializers
from django.db import models
from django.db import utils

from djangodemo.models.Matchup import Matchup
from djangodemo.models.Game import Game
from djangodemo.exceptions import Exceptions

 #======================================================================
# 
# Encapsulates data for model Matchup
#
# @author 
#
#======================================================================

#======================================================================
# Class MatchupDelegate Declaration
#======================================================================
class MatchupDelegate :

#======================================================================
# Function Declarations
#======================================================================

	def get(self, matchupId ):
		try:	
			matchup = Matchup.objects.filter(id=matchupId)
			return matchup.first();
		except Matchup.DoesNotExist:
			raise ProcessingError("Matchup with id " + str(matchupId) + " does not exist.")
		except utils.DatabaseError:
			raise StorageReadError()
		except Exception:
			raise GeneralError(errMsg) 

	def createFromJson(self, matchup):
		for model in serializers.deserialize("json", matchup):
			model.save()
			return model;

	def create(self, matchup):
		matchup.save()
		return matchup;

	def saveFromJson(self, matchup):
		for model in serializers.deserialize("json", matchup):
			model.save()
			return matchup;
	
	def save(self, matchup):
		matchup.save()
		return matchup;
	
	def delete(self, matchupId ):
		errMsg = "Failed to delete Matchup from db using id " + str(matchupId)
		
		try:
			matchup = Matchup.objects.get(id=matchupId)
			matchup.delete()
			return True
		except Matchup.DoesNotExist:
			raise ProcessingError("Matchup with id " + str(matchupId) + " does not exist.")
		except utils.DatabaseError:
			raise StorageReadError()
		except Exception:
			raise GeneralError(errMsg) 
	
	def getAll(self):
		try:
			all = Matchup.objects.all()
			return all;
		except utils.DatabaseError:
			raise StorageReadError("Failed to get all Matchup from db")
		except Exception:
			return None;
		
