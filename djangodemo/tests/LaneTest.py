import datetime

from django.test import TestCase
from django.utils import timezone
from djangodemo.models.Lane import Lane
from djangodemo.delegates.LaneDelegate import LaneDelegate

 #======================================================================
# 
# Encapsulates data for model Lane
#
# @author 
#
#======================================================================

#======================================================================
# Class LaneTest Declaration
#======================================================================
class LaneTest (TestCase) :
	def test_crud(self) :
		lane = Lane()
		lane.number = "default number field value"
		
		delegate = LaneDelegate()
		responseObj = delegate.create(lane)
		
		self.assertEqual(responseObj, delegate.get( responseObj.id ))
	
		allObj = delegate.getAll()
		self.assertEqual(allObj.count(), 1 )		
		delegate.delete(responseObj.id)
		
		allObj = delegate.getAll()
		self.assertEqual(allObj.count(), 0 )		


