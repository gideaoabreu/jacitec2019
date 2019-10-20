from rest_framework import serializers
from app.models import Palestra


class PalestraSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Palestra
        fields = ['id',
                  'titulo',
                  'data',
                  'hora_inicio',
                  'hora_fim',
                  'palestrantes',
                  'categoria',
                  'vagas_total',
                  'vagas_restantes',
                  'local']
