from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email','contact_date')
    search_fields = ('email',)
    list_filter = ('contact_date',)
    ordering = ('contact_date', 'email')

admin.site.register(Contact, ContactAdmin)
