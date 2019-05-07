import datetime

from django.test import TestCase
from django.utils import timezone
from djangodemo.models.Matchup import Matchup
from djangodemo.delegates.MatchupDelegate import MatchupDelegate

 #======================================================================
# 
# Encapsulates data for model Matchup
#
# @author 
#
#======================================================================

#======================================================================
# Class MatchupTest Declaration
#======================================================================
class MatchupTest (TestCase) :
	def test_crud(self) :
		matchup = Matchup()
		matchup.name = "default name field value"
		
		delegate = MatchupDelegate()
		responseObj = delegate.create(matchup)
		
		self.assertEqual(responseObj, delegate.get( responseObj.id ))
	
		allObj = delegate.getAll()
		self.assertEqual(allObj.count(), 1 )		
		delegate.delete(responseObj.id)
		
		allObj = delegate.getAll()
		self.assertEqual(allObj.count(), 0 )		


