from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.decorators import login_required
from django.utils.crypto import get_random_string
from .models import Payment
from .forms import PaymentForm
import random

def login_view(request):
    error_message = None  # Initialize error message variable

    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect("payment_page")  # Redirect to payment page after login
        else:
            error_message = "Invalid email or password. Please try again."

    return render(request, "login.html", {"error": error_message})  # Pass error to template

@login_required
def payment_page(request):
    if request.method == "POST":
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save()
            request.session['payment_id'] = payment.id  # Store payment ID for OTP verification
            return redirect('otp_page')  # Redirect to OTP page
    else:
        form = PaymentForm()
    
    return render(request, "payment.html", {"form": form})

@login_required
def otp_page(request):
    if request.method == "POST":
        otp = (
            request.POST.get("otp1", "") +
            request.POST.get("otp2", "") +
            request.POST.get("otp3", "") +
            request.POST.get("otp4", "") +
            request.POST.get("otp5", "") +
            request.POST.get("otp6", "")
        )

        if otp:  # Accept any input as a valid OTP
            return redirect('success_page')  # Redirect to success page
        
        else:
            return render(request, 'otp.html', {"error": "Please enter OTP"})

    return render(request, 'otp.html')

@login_required
def success_view(request):
    return render(request, 'success.html')
