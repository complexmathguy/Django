from django.db import models
#======================================================================
# 
# Encapsulates data for model Matchup
#
# @author 
#
#======================================================================

#======================================================================
# Class Matchup Declaration
#======================================================================
class Matchup (models.Model):

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
		return "Matchup";
    
	def objectType(self):
		return "Matchup";
