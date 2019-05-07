from django.db import models
#======================================================================
# 
# Encapsulates data for model Lane
#
# @author 
#
#======================================================================

#======================================================================
# Class Lane Declaration
#======================================================================
class Lane (models.Model):

#======================================================================
# attribute declarations
#======================================================================
	number = models.CharField(max_length=64, null=True)

#======================================================================
# function declarations
#======================================================================
	def toString(self):
		str = ""
		str = str + self.number
		return str;
    
	def __str__(self):
		return self.toString();

	def identity(self):
		return "Lane";
    
	def objectType(self):
		return "Lane";
