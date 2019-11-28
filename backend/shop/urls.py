from django.conf.urls import url
from shop import views
 
urlpatterns = [
    
    url('12', views.EffectList.as_view(),name='listall'),
    url('distortion', views.DistortionEffectList.as_view(), name='distortion'),
    url('compressor', views.CompressorEffectList.as_view(), name='compressor'),
    url('octave', views.OctaveEffectList.as_view(), name='octave'),
    url('statue',views.view_statue, name="statue"),
    url('policy',views.view_policy, name="policy"),
    url('delivery',views.view_delivery, name="delivery"),
    url('contact',views.contact_form, name="contact"),


    url(r'^$', views.product_list,
        name='list'),
    url(r'^(?P<product_id>\d+)/(?P<slug>[-\w]+)/$',
        views.product_detail,
        name='product_detail')
]