from django.urls import path
from .views import login_view, payment_page, success_view, otp_page

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', login_view, name='login_page'),
    path('payment/', payment_page, name='payment_page'),
    path('otp/', otp_page, name='otp_page'),
    path('success/', success_view, name='success_page'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]
