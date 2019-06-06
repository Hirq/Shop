from django.conf.urls import url
from shop import views
 
urlpatterns = [
    # url(r'^$', views.HomePageView.as_view()),
    # url(r'^getcust/$',views.Customers.getCust),
    
    url('index', views.EffectList.as_view(),name='index'),
    url('distortion', views.DistortionEffectList.as_view(), name='distortion'),
    url('compressor', views.CompressorEffectList.as_view(), name='compressor'),
    url('octave', views.OctaveEffectList.as_view(), name='octave'),

    # url('links', views.EffectList.as_view(), name='links')
]