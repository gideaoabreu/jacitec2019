from rest_framework import serializers
from app.models import Palestra


class PaletraSerializer(serializers.HyperlinkedModelSerializer):
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
