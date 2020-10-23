from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email','date')
    search_fields = ('email',)
    list_filter = ('date',)
    ordering = ('date', 'email')

admin.site.register(Contact, ContactAdmin)
