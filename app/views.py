from rest_framework import viewsets
from app.serializers import PalestraSerializer
from app.models import Palestra


class PalestraViewSet(viewsets.ModelViewSet):
    queryset = Palestra.objects.all().order_by('data', 'hora_inicio')
    serializer_class = PalestraSerializer
