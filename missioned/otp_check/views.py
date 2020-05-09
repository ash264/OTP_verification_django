from django.shortcuts import render

import requests
from django.contrib.auth.models import User
from django.http import JsonResponse

def home(request):
	return render(request,'home.html')

def enter(request):
	return render(request,'enter.html')

def send_otp(request):
	response_data = {}
	if request.method == "POST" and request.is_ajax:
		user_phone = request.POST['phone_number']

		# 2factor APIKey: 5608d716-90ef-11ea-9fa5-0200cd936042 (50 free sms)
		
		# APIKey: "5608d716-90ef-11ea-9fa5-0200cd936042"		
		url = "http://2factor.in/API/V1/" + APIKey + "/SMS/" + "+91" + user_phone + "/AUTOGEN/OTPSEND"

		response = requests.request("GET", url)
		data = response.json()
		request.session['otp_session_data'] = data['Details']
		# otp_session_data is stored in session.
		response_data = {'Message':'Success'}
	else:
		response_data = {'Message':'Failed'}

	return JsonResponse(response_data)




def otp_verification(request):
	response_data = {}
	if request.method == "POST" and request.is_ajax:
		user_otp = request.POST['otp']
		
		# APIKey: "5608d716-90ef-11ea-9fa5-0200cd936042"
		url = "http://2factor.in/API/V1/" + APIKey + "/SMS/VERIFY/" + request.session['otp_session_data'] + "/" + user_otp + ""
		# otp_session_data is fetched from session.
		response = requests.request("GET", url)		
		data = response.json()
		if data['Status'] == "Success":
			# logged_user.is_active = True
			response_data = {'Message':'Success'}
		else:
			response_data = {'Message':'Failed'}
			# logout(request)
	return JsonResponse(response_data)
