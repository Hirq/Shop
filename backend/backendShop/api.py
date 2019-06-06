from rest_framework import routers
from shop import api_views as myapp_views

router = routers.DefaultRouter()
router.register(r'effect', myapp_views.EffectViewSet, 'effect')
router.register(r'compressor',myapp_views.CompressorViewSet, 'compressor')
router.register(r'distortion',myapp_views.DistortionViewSet, 'distortion')
router.register(r'octave',myapp_views.OctaveViewSet, 'octave')
