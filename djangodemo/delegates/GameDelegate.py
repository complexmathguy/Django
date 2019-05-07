from django.core import exceptions
from django.core import serializers
from django.db import models
from django.db import utils

from djangodemo.models.Game import Game
from djangodemo.models.Matchup import Matchup
from djangodemo.models.Player import Player
from djangodemo.exceptions import Exceptions

 #======================================================================
# 
# Encapsulates data for model Game
#
# @author 
#
#======================================================================

#======================================================================
# Class GameDelegate Declaration
#======================================================================
class GameDelegate :

#======================================================================
# Function Declarations
#======================================================================

	def get(self, gameId ):
		try:	
			game = Game.objects.filter(id=gameId)
			return game.first();
		except Game.DoesNotExist:
			raise ProcessingError("Game with id " + str(gameId) + " does not exist.")
		except utils.DatabaseError:
			raise StorageReadError()
		except Exception:
			raise GeneralError(errMsg) 

	def createFromJson(self, game):
		for model in serializers.deserialize("json", game):
			model.save()
			return model;

	def create(self, game):
		game.save()
		return game;

	def saveFromJson(self, game):
		for model in serializers.deserialize("json", game):
			model.save()
			return game;
	
	def save(self, game):
		game.save()
		return game;
	
	def delete(self, gameId ):
		errMsg = "Failed to delete Game from db using id " + str(gameId)
		
		try:
			game = Game.objects.get(id=gameId)
			game.delete()
			return True
		except Game.DoesNotExist:
			raise ProcessingError("Game with id " + str(gameId) + " does not exist.")
		except utils.DatabaseError:
			raise StorageReadError()
		except Exception:
			raise GeneralError(errMsg) 
	
	def getAll(self):
		try:
			all = Game.objects.all()
			return all;
		except utils.DatabaseError:
			raise StorageReadError("Failed to get all Game from db")
		except Exception:
			return None;
		
