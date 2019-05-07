from django.core import exceptions
from django.core import serializers
from django.db import models
from django.db import utils

from djangodemo.models.Alley import Alley
from djangodemo.models.League import League
from djangodemo.models.Tournament import Tournament
from djangodemo.models.Lane import Lane
from djangodemo.exceptions import Exceptions

 #======================================================================
# 
# Encapsulates data for model Alley
#
# @author 
#
#======================================================================

#======================================================================
# Class AlleyDelegate Declaration
#======================================================================
class AlleyDelegate :

#======================================================================
# Function Declarations
#======================================================================

	def get(self, alleyId ):
		try:	
			alley = Alley.objects.filter(id=alleyId)
			return alley.first();
		except Alley.DoesNotExist:
			raise ProcessingError("Alley with id " + str(alleyId) + " does not exist.")
		except utils.DatabaseError:
			raise StorageReadError()
		except Exception:
			raise GeneralError(errMsg) 

	def createFromJson(self, alley):
		for model in serializers.deserialize("json", alley):
			model.save()
			return model;

	def create(self, alley):
		alley.save()
		return alley;

	def saveFromJson(self, alley):
		for model in serializers.deserialize("json", alley):
			model.save()
			return alley;
	
	def save(self, alley):
		alley.save()
		return alley;
	
	def delete(self, alleyId ):
		errMsg = "Failed to delete Alley from db using id " + str(alleyId)
		
		try:
			alley = Alley.objects.get(id=alleyId)
			alley.delete()
			return True
		except Alley.DoesNotExist:
			raise ProcessingError("Alley with id " + str(alleyId) + " does not exist.")
		except utils.DatabaseError:
			raise StorageReadError()
		except Exception:
			raise GeneralError(errMsg) 
	
	def getAll(self):
		try:
			all = Alley.objects.all()
			return all;
		except utils.DatabaseError:
			raise StorageReadError("Failed to get all Alley from db")
		except Exception:
			return None;
		
