from django.shortcuts import render
from .models import About, Index, Services, BulletPoint

def index(request):
    index = Index.objects.all()
    return render(request, 'index.html', {"index":index})

def services(request):
    services = Services.object.all()
    bullet = BulletPoint.object.all()
    return render(request, 'sevices.html', {"services":services, "bullet":bullet})

def about(request):
    about = About.objects.all()
    return render(request, 'about.html', {"about":about})