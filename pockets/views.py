from rest_framework.viewsets import ModelViewSet
from .models import Pocket
from .serializers import PocketSerializer
from django_filters.rest_framework import DjangoFilterBackend


class PocketViewSet(ModelViewSet):
    queryset = Pocket.objects.all()
    serializer_class = PocketSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["user"]
    lookup_field = "id"
