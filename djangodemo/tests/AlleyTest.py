import datetime

from django.test import TestCase
from django.utils import timezone
from djangodemo.models.Alley import Alley
from djangodemo.delegates.AlleyDelegate import AlleyDelegate

 #======================================================================
# 
# Encapsulates data for model Alley
#
# @author 
#
#======================================================================

#======================================================================
# Class AlleyTest Declaration
#======================================================================
class AlleyTest (TestCase) :
	def test_crud(self) :
		alley = Alley()
		alley.name = "default name field value"
		
		delegate = AlleyDelegate()
		responseObj = delegate.create(alley)
		
		self.assertEqual(responseObj, delegate.get( responseObj.id ))
	
		allObj = delegate.getAll()
		self.assertEqual(allObj.count(), 1 )		
		delegate.delete(responseObj.id)
		
		allObj = delegate.getAll()
		self.assertEqual(allObj.count(), 0 )		


