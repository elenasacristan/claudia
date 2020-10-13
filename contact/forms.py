from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter your name *'}))
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter your email *'}))
    phone = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter your phone *' }))
    message = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'How can I help you? *'}))
    
    class Meta:
        model =  Contact
        fields = ("name", "email", "phone", "message")
