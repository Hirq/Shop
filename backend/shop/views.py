from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from .models import Effect
from django.views import generic


class EffectList(generic.ListView):
    template_name = 'shop/index.html'
    context_object_name = 'firstlist'

    def get_queryset(self):
        return Effect.objects.all()


class DistortionEffectList(generic.ListView):
    template_name = 'shop/distortion.html'
    context_object_name = 'distlist'

    def get_queryset(self):
        return Effect.objects.all()


class OctaveEffectList(generic.ListView):
    template_name = 'shop/octave.html'
    context_object_name = 'octavelist'

    def get_queryset(self):
        return Effect.objects.all()

class CompressorEffectList(generic.ListView):
    template_name = 'shop/compressor.html'
    context_object_name = 'compressorlist'

    def get_queryset(self):
        return Effect.objects.all()