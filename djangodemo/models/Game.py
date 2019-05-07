from django.db import models
#======================================================================
# 
# Encapsulates data for model Game
#
# @author 
#
#======================================================================

#======================================================================
# Class Game Declaration
#======================================================================
class Game (models.Model):

#======================================================================
# attribute declarations
#======================================================================
	frames = models.CharField(max_length=64, null=True)

#======================================================================
# function declarations
#======================================================================
	def toString(self):
		str = ""
		str = str + self.frames
		return str;
    
	def __str__(self):
		return self.toString();

	def identity(self):
		return "Game";
    
	def objectType(self):
		return "Game";
