from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

from django.db import models

class Payment(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    zipcode = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    card_name = models.CharField(max_length=255, blank=True, null=True)
    card_number = models.CharField(max_length=16, blank=True, null=True)
    cvv = models.CharField(max_length=3, blank=True, null=True)
    expiry_month = models.CharField(max_length=2, blank=True, null=True)
    expiry_year = models.CharField(max_length=4, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    payment_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f"{self.name or 'Unknown'} - {self.card_number[-4:] if self.card_number else 'XXXX'}"


class UserCredentials(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Store hashed password for security
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
