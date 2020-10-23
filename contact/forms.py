from django import forms
from .models import Contact
from django.core.exceptions import ValidationError

class ContactForm(forms.ModelForm):
    name = forms.CharField(required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your name *'}))
    email = forms.CharField(required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your email *'}))
    phone = forms.CharField(required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your phone' }))
    message = forms.CharField(required=False,
        widget=forms.Textarea(attrs={'placeholder': 'How can I help you? *'}))
    
    class Meta:
        model =  Contact
        fields = ["name", "email", "phone", "message"]

    # email validation
    def clean_name(self):
        name = self.cleaned_data.get('name')
                
        if not name:
            print('not name')
            raise forms.ValidationError('This field is required')
        print('yes name')
        return name

    # email validation
    def clean_email(self):
        email = self.cleaned_data.get('email')
                
        if not email:
            raise forms.ValidationError('Please enter a valid email')
        return email

    # content validation
    def clean_message(self):
        message = self.cleaned_data.get('message')
                
        if not message:
            raise forms.ValidationError('This field is required')
        return message

