from django.db import models
#======================================================================
# 
# Encapsulates data for model Alley
#
# @author 
#
#======================================================================

#======================================================================
# Class Alley Declaration
#======================================================================
class Alley (models.Model):

#======================================================================
# attribute declarations
#======================================================================
	name = models.CharField(max_length=200, null=True)

#======================================================================
# function declarations
#======================================================================
	def toString(self):
		str = ""
		str = str + self.name
		return str;
    
	def __str__(self):
		return self.toString();

	def identity(self):
		return "Alley";
    
	def objectType(self):
		return "Alley";
