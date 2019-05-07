from django.core import exceptions
from django.core import serializers
from django.db import models
from django.db import utils

from djangodemo.models.Lane import Lane
from djangodemo.exceptions import Exceptions

 #======================================================================
# 
# Encapsulates data for model Lane
#
# @author 
#
#======================================================================

#======================================================================
# Class LaneDelegate Declaration
#======================================================================
class LaneDelegate :

#======================================================================
# Function Declarations
#======================================================================

	def get(self, laneId ):
		try:	
			lane = Lane.objects.filter(id=laneId)
			return lane.first();
		except Lane.DoesNotExist:
			raise ProcessingError("Lane with id " + str(laneId) + " does not exist.")
		except utils.DatabaseError:
			raise StorageReadError()
		except Exception:
			raise GeneralError(errMsg) 

	def createFromJson(self, lane):
		for model in serializers.deserialize("json", lane):
			model.save()
			return model;

	def create(self, lane):
		lane.save()
		return lane;

	def saveFromJson(self, lane):
		for model in serializers.deserialize("json", lane):
			model.save()
			return lane;
	
	def save(self, lane):
		lane.save()
		return lane;
	
	def delete(self, laneId ):
		errMsg = "Failed to delete Lane from db using id " + str(laneId)
		
		try:
			lane = Lane.objects.get(id=laneId)
			lane.delete()
			return True
		except Lane.DoesNotExist:
			raise ProcessingError("Lane with id " + str(laneId) + " does not exist.")
		except utils.DatabaseError:
			raise StorageReadError()
		except Exception:
			raise GeneralError(errMsg) 
	
	def getAll(self):
		try:
			all = Lane.objects.all()
			return all;
		except utils.DatabaseError:
			raise StorageReadError("Failed to get all Lane from db")
		except Exception:
			return None;
		
