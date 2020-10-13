from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.utils import timezone
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)    
    
        if contact_form.is_valid():
            form = contact_form.save(commit=False)
            form.contact_date = timezone.now()
            form.save()
            text = "Thanks {}, I have received your message!".format(form.name)
            messages.success(request, text)
            return redirect(reverse('index'))

    else:
        contact_form = ContactForm()

    return render(request, "contact.html", {"contact_form":contact_form})
