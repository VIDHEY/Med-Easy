from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from .models import *
from django.http import JsonResponse
from random import randint
from .sms_send import send_message
from django.utils import timezone
from .disease_pred import predict

import pandas as pd
import numpy as np
from sklearn.naive_bayes import MultinomialNB
from sklearn.cross_validation import train_test_split
import os
from django.conf import settings

file_path=os.path.join(settings.STATIC_ROOT, 'data_pivoted.csv')
data = pd.read_csv(file_path)
data = data.fillna(0)
cols = data.columns.tolist()
cols.remove('disease')
x = data[cols]
y = data.disease
mnb = MultinomialNB()
mnb = mnb.fit(x, y)
dict_ = {}
i=0
for dat in data.iloc[[0]]:
	dict_[dat]=i
	i += 1

def predict(lis):	
	x1 = np.zeros(len(cols))
	for sym in lis:
		x1[dict_[sym]-1]=1
	x1=x1.reshape(1, -1)
	y1=mnb.predict(x1)
	pred=''.join(y1)
	return pred



def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def home(request):
	return render(request, 'index.html')

def login_form(request):
	if request.method=='POST':
		ph_num=request.POST['phone_number']
		user=User.objects.get(phone_number=ph_num)
		if user.phone_number==request.POST['passwd']:
			login(request,user)
			return redirect('')
		else:
			data={
			'error':'Wrong Password!!'
			}
			return JsonResponse(data)
	else:
		return redirect('')

def signup_otp_generation(request):
	if request.method=='POST':
		ph_num=request.POST['phone_number']
		if User.objects.get(phone_number=ph_num):
			data={
			'error':'<div>Number already exists!</div>'
			}
			return JsonResponse(data)
		else:
			pin=random_with_N_digits(4)
			content="Your One Time Password is"+pin
			send_message(ph_num,content)
			session=SessionDoctorAccount(time_of_issue=timezone.now(),phone_number=ph_num)
			session.save()
			data={
			'html':'<div>Enter OTP!!</div>'
			}
			return JsonResponse(data)

def signup_otp_verification(request):
	request.user

def show_patient_profile(request):
	if request.method=='POST':
		doctor_first_name=request.user.first_name
		doctor_second_name=request.user.second_name
		ph_num=request.POST['phone_number']
		if User.objects.get(phone_number=ph_num):
			user=User.objects.get(phone_number=ph_num)
			if user.is_patient==True:
				pin=random_with_N_digits(4)
				content="Dr. "+doctor_first_name+" "+doctor_second_name+" wants to see and edit your detail. To give access share this One Time Password with him: "+pin
				send_message(ph_num,content)
				# Json response of a html division
				data={
				'html':'<div>Enter otp!!</div>'
				}
				return JsonResponse(data)

		data={
		'error': 'No account related to this phone_number'
		}
		return JsonResponse(data)



def prediction(request):
	sym_list=request.GET.getlist('sym_list[]')
	disease_pred=predict(sym_list)
	data={
	'disease_prediction':disease_pred
	}
	return JsonResponse(data)

def prediction_form(request):
	return render(request,'disease_prediction.html')