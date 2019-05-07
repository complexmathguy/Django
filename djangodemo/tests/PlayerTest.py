import datetime

from django.test import TestCase
from django.utils import timezone
from djangodemo.models.Player import Player
from djangodemo.delegates.PlayerDelegate import PlayerDelegate

 #======================================================================
# 
# Encapsulates data for model Player
#
# @author 
#
#======================================================================

#======================================================================
# Class PlayerTest Declaration
#======================================================================
class PlayerTest (TestCase) :
	def test_crud(self) :
		player = Player()
		player.name = "default name field value"
		player.dateOfBirth = "default dateOfBirth field value"
		player.height = "default height field value"
		player.isProfessional = "default isProfessional field value"
		
		delegate = PlayerDelegate()
		responseObj = delegate.create(player)
		
		self.assertEqual(responseObj, delegate.get( responseObj.id ))
	
		allObj = delegate.getAll()
		self.assertEqual(allObj.count(), 1 )		
		delegate.delete(responseObj.id)
		
		allObj = delegate.getAll()
		self.assertEqual(allObj.count(), 0 )		


