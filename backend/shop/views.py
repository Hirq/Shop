from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponse
from .models import Effect
from django.views import generic
from django.shortcuts import render, get_object_or_404
from cart.forms import CartAddEffectForm
from .forms import MessageForm

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

def product_list(request, category_slug=None):
    products = Effect.objects.all()

    return render(request,
                  'shop/list.html',
                  {'products': products})


def product_detail(request, product_id, slug):
    product = get_object_or_404(Effect,
                                effect_id=product_id)
    cart_product_form = CartAddEffectForm()
    return render(request,
                  'shop/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})

def view_statue(request):
    return render(request, 'shop/statue.html')

def view_policy(request):
    return render(request, 'shop/privacy_policy.html')

def view_delivery(request):
    return render(request, 'shop/delivery.html')

def contact_form(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()

            return redirect('/')
    else:
        form = MessageForm()

    return render(request, 'shop/contact.html', {'form': form})