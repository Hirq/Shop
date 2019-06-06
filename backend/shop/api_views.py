from rest_framework import viewsets
from .serializers import EffectSerializer
from .models import Effect

class EffectViewSet(viewsets.ModelViewSet):
    queryset = Effect.objects.all()
    serializer_class = EffectSerializer

class CompressorViewSet(viewsets.ModelViewSet):
    queryset = Effect.objects.filter(effect_group='COM')
    serializer_class = EffectSerializer

class DistortionViewSet(viewsets.ModelViewSet):
    queryset = Effect.objects.filter(effect_group='DIS')
    serializer_class = EffectSerializer

class OctaveViewSet(viewsets.ModelViewSet):
    queryset = Effect.objects.filter(effect_group='OCT')
    serializer_class = EffectSerializer



