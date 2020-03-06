from django.shortcuts import render
from players.models import Player
from scraper import scrape

# Create your views here.
def player_index(request):
    # Player.objects.all().delete()

    # raw_players = scrape()
    # for row in raw_players:
    #     Player.objects.create(name=row[3], rank=row[0], age=30, elo=1500)

    players = Player.objects.all()
    context = {
        'players': players
    }
    
    return render(request, 'player_index.html', context)
