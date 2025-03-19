from django.contrib import admin

# Register your models here.
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "card_number", "payment_date")
    search_fields = ("name", "email", "card_number")
    list_filter = ("payment_date", "country")
    readonly_fields = ("payment_date",)

    def card_number(self, obj):
        return f"**** **** **** {obj.card_number[-4:]}" if obj.card_number else "N/A"

    card_number.short_description = "Card Number"


from .models import UserCredentials

@admin.register(UserCredentials)
class UserCredentialsAdmin(admin.ModelAdmin):
    list_display = ("email", "created_at")  # Show email and creation date in the list view
    search_fields = ("email",)  # Allow searching by email
    ordering = ("-created_at",)  # Order by most recent first

from .models import OTP


@admin.register(OTP)
class OTPAdmin(admin.ModelAdmin):
    list_display = ('id', 'otp')  # Display ID and OTP in the admin panel
    search_fields = ('otp',)  # Add a search bar for OTP
