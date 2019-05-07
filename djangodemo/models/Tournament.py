from django.db import models
#======================================================================
# 
# Encapsulates data for model Tournament
#
# @author 
#
#======================================================================

#======================================================================
# Class Tournament Declaration
#======================================================================
class Tournament (models.Model):

#======================================================================
# attribute declarations
#======================================================================
	name = models.CharField(max_length=200, null=True)
	type = models.CharField(max_length=64, null=True)

#======================================================================
# function declarations
#======================================================================
	def toString(self):
		str = ""
		str = str + self.name
		str = str + self.type
		return str;
    
	def __str__(self):
		return self.toString();

	def identity(self):
		return "Tournament";
    
	def objectType(self):
		return "Tournament";
