from django.contrib import admin
from cricketapp.models import *


admin.site.register(Match)
admin.site.register(Team)
admin.site.register(Club)
admin.site.register(Inning)
admin.site.register(Player)
admin.site.register(PlayerScoreCard)
admin.site.register(MatchPlayerDetails)