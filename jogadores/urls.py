from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_jogadores),
    path('adicionar/', views.adicionar_jogador),
    path('editar/<int:id>/', views.editar_jogador),
    path('excluir/<int:id>/', views.excluir_jogador),
]
