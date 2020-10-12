from django.shortcuts import render
from .models import About, Index, Services, BulletPoint

def index(request):
    index = Index.objects.all()[0]
    return render(request, 'index.html', {"index":index})

def services(request):
    services = Services.objects.all()
    bullets = BulletPoint.objects.all()
    return render(request, 'services.html', {"services":services, "bullets":bullets})

def about(request):
    about = About.objects.all()[0]
    return render(request, 'about.html', {"about":about})