from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from .models import Checkpoint
from .serializers import CheckpointSerializers
from django_filters.rest_framework import DjangoFilterBackend


class CheckpointViewSet(ModelViewSet):
    queryset = Checkpoint.objects.all()
    serializer_class = CheckpointSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["user"]
    lookup_field = "user_id"

    def list(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.user != request.user:
            return Response({'detail': 'Permission denied.'}, status=status.HTTP_403_FORBIDDEN)
        
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
