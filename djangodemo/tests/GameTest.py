import datetime

from django.test import TestCase
from django.utils import timezone
from djangodemo.models.Game import Game
from djangodemo.delegates.GameDelegate import GameDelegate

 #======================================================================
# 
# Encapsulates data for model Game
#
# @author 
#
#======================================================================

#======================================================================
# Class GameTest Declaration
#======================================================================
class GameTest (TestCase) :
	def test_crud(self) :
		game = Game()
		game.frames = "default frames field value"
		
		delegate = GameDelegate()
		responseObj = delegate.create(game)
		
		self.assertEqual(responseObj, delegate.get( responseObj.id ))
	
		allObj = delegate.getAll()
		self.assertEqual(allObj.count(), 1 )		
		delegate.delete(responseObj.id)
		
		allObj = delegate.getAll()
		self.assertEqual(allObj.count(), 0 )		


