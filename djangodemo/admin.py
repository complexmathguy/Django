from django.contrib import admin

# Register your models here.
from .models.Alley import Alley
from .models.Game import Game
from .models.Lane import Lane
from .models.League import League
from .models.Matchup import Matchup
from .models.Player import Player
from .models.Tournament import Tournament

# Need to add this for each model that requires managing

admin.site.register(Alley)
admin.site.register(Game)
admin.site.register(Lane)
admin.site.register(League)
admin.site.register(Matchup)
admin.site.register(Player)
admin.site.register(Tournament)
