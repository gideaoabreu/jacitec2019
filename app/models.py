from django.db import models


class Palestra(models.Model):
    titulo = models.CharField(max_length=50)
    data = models.DateField()
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()
    palestrantes = models.CharField(max_length=100)
    categoria = models.CharField(max_length=30)
    vagas_total = models.IntegerField()
    vagas_restantes = models.IntegerField()
    local = models.CharField(max_length=100)
