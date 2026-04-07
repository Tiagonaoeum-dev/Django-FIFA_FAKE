from django.shortcuts import render, redirect, get_object_or_404
from .models import Jogador
from .forms import JogadorForm


def lista_jogadores(request):
    jogadores = Jogador.objects.all()
    return render(request, 'jogadores/lista.html', {'jogadores': jogadores})


def adicionar_jogador(request):
    if request.method == 'POST':
        form = JogadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = JogadorForm()

    return render(request, 'jogadores/adicionar.html', {'form': form})


def editar_jogador(request, id):
    jogador = get_object_or_404(Jogador, id=id)

    if request.method == 'POST':
        form = JogadorForm(request.POST, instance=jogador)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = JogadorForm(instance=jogador)

    return render(request, 'jogadores/adicionar.html', {'form': form})


def excluir_jogador(request, id):
    jogador = get_object_or_404(Jogador, id=id)

    if request.method == 'POST':
        jogador.delete()
        return redirect('/')

    return render(request, 'jogadores/excluir.html', {'jogador': jogador})
