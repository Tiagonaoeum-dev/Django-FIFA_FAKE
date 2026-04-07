from django.db import models

class Jogador(models.Model):
    nome = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    posicao = models.CharField(max_length=10)
    overall = models.IntegerField()

    pace = models.IntegerField()
    shooting = models.IntegerField()
    passing = models.IntegerField()
    dribbling = models.IntegerField()
    defense = models.IntegerField()
    physical = models.IntegerField()

    def __str__(self):
        return self.nome
