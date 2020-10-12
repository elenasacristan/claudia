from django.contrib import admin
from .models import Index, About, Services, BulletPoint

# Register your models here.
admin.site.register(Index)
admin.site.register(About)
admin.site.register(Services)
admin.site.register(BulletPoint)