from django.db import models
from datetime import datetime

class Contact(models.Model):

    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15, blank=True)
    message = models.TextField()
    contact_date = models.DateField(default=datetime.now)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Emails"
        ordering = ('contact_date',)

    # email validation
    def clean_name(self):
                name = self.cleaned_data.get('name')
                
                if not name:
                    raise forms.ValidationError(u'This field is required..')
                return name

    # email validation
    def clean_email(self):
                email = self.cleaned_data.get('email')
                
                if not email:
                    raise forms.ValidationError(u'This field is required.')
                return email

    # content validation
    def clean_message(self):
                message = self.cleaned_data.get('message')
                
                if not message:
                    raise forms.ValidationError(u'This field is required.')
                return message

