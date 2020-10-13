from django.db import models

class Contact(models.Model):

    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15)
    message = models.TextField()

    class Meta:
        verbose_name_plural = "Contact_emails"

    def __str__(self):
        return self.name

