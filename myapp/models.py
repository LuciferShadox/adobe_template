from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

from django.db import models

class Payment(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.TextField()
    zipcode = models.CharField(max_length=10)
    country = models.CharField(max_length=50)
    card_name = models.CharField(max_length=255)
    card_number = models.CharField(max_length=16)
    cvv = models.CharField(max_length=3)
    expiry_month = models.CharField(max_length=2)
    expiry_year = models.CharField(max_length=4)
    phone = models.CharField(max_length=15, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.card_number[-4:]}"
