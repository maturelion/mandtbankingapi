from rest_framework.viewsets import ModelViewSet
from .models import Wallet
from .serializers import WalletSerializer
from django_filters.rest_framework import DjangoFilterBackend


class WalletViewSet(ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["user"]
    lookup_field = "id"
