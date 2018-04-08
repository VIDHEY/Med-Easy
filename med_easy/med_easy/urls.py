"""med_easy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from account import views
from django.conf.urls.static import static
from .settings import *

urlpatterns = [
    path('',views.home,name='home'),
    path('home/',views.home,name='home'),
    path('prediction/', views.prediction_form,name='prediction_form'),
    path('ajax/prediction_result/', views.prediction,name='prediction'),
    # path('profile/',views.show_self_profile, name='show_self_profile'),
    path('patient/',views.show_patient_profile, name='show_patient_profile'),
    # path('ajax/signup/otp_generation/',views.signup_otp_generation, name='signup_otp_generation'),
    # path('ajax/signup/otp_verification/',views.signup_otp_verify, name='signup_otp_verification'),
    # path('ajax/signup/activate_user',views.activate_user, name='activate_user'),
    path('ajax/login_form/', views.login_form, name='login_form'),
    # path('ajax/login_submit', views.login_submit, name='login_submit')
    path('doctor_search/', views.doctor_search, name='doctor_search'),
]+static(STATIC_URL,document_root=STATIC_ROOT)
