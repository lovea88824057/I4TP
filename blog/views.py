from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from . import models
from django.shortcuts import render_to_response


def index(request):
    products = models.Product.objects.all() # here, product is just a variable, all back is a list
    return render(request, 'blog/index.html', {'products': products})

def indexmaschine(request):
    maschines = models.Maschine.objects.all()
    return render(request, 'blog/indexmaschine.html', {'maschines': maschines})


def dashboard(request):
    total = models.Product.objects.count()
    upline = models.Product.objects.filter(oee__gte=90).filter(oee__lte=100).count()
    offline = models.Product.objects.filter(oee__gte=60).filter(oee__lt=90).count()
    breakdown = models.Product.objects.filter(oee__gte=0).filter(oee__lt=60).count()
    # backup = models.Asset.objects.filter(status=4).count()
    up_rate = round(upline/total*100)
    o_rate = round(offline/total*100)
    # un_rate = round(unknown/total*100)
    bd_rate = round(breakdown/total*100)

    p_number = models.Product.objects.count()
    m_number = models.Maschine.objects.count()


    return render(request, 'blog/dashboard.html', locals())


def search_results(request):
    oee = request.GET['oee']
    quality = request.GET['quality']
    volume = request.GET['volume']
    x = request.GET['x']
    y = request.GET['y']
    z = request.GET['z']
    material = request.GET['material']
    result = models.Componentmaschine.objects.filter(oee_componentofmaschine__gte=oee).filter(quality__gte=quality).filter(volume__exact=volume).filter(length_workspace__gte=x).filter(width_workspace__gte=y).filter(height_workspace__gte=z).filter(material_tool__exact=material)
    return render(request, 'blog/search_results.html', locals())


def requirement(request):
    return render(request, 'blog/requirement.html')