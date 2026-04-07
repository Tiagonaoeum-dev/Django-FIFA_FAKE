from django.shortcuts import render
from .models import Jogador

def lista_jogadores(request):
    jogadores = Jogador.objects.all()
    return render(request, 'jogadores/lista.html', {'jogadores': jogadores})
