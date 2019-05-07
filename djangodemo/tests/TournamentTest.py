import datetime

from django.test import TestCase
from django.utils import timezone
from djangodemo.models.Tournament import Tournament
from djangodemo.delegates.TournamentDelegate import TournamentDelegate

 #======================================================================
# 
# Encapsulates data for model Tournament
#
# @author 
#
#======================================================================

#======================================================================
# Class TournamentTest Declaration
#======================================================================
class TournamentTest (TestCase) :
	def test_crud(self) :
		tournament = Tournament()
		tournament.name = "default name field value"
		tournament.type = "default type field value"
		
		delegate = TournamentDelegate()
		responseObj = delegate.create(tournament)
		
		self.assertEqual(responseObj, delegate.get( responseObj.id ))
	
		allObj = delegate.getAll()
		self.assertEqual(allObj.count(), 1 )		
		delegate.delete(responseObj.id)
		
		allObj = delegate.getAll()
		self.assertEqual(allObj.count(), 0 )		


