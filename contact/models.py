from django.db import models
from datetime import datetime

class Contact(models.Model):

    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15, blank=True)
    message = models.TextField()
    date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Emails"
        ordering = ('date',)
