from rest_framework import viewsets
from app.serializers import PaletraSerializer
from app.models import Palestra


class PaletraViewSet(viewsets.ModelViewSet):
    queryset = Palestra.objects.all().order_by('data', 'hora_inicio')
    serializer_class = PaletraSerializer
