from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import MSAT
import datetime

@csrf_exempt
def home(request):
	context = {}
	if request.method == 'POST':
		print(request.POST)

		obj = MSAT(
			r_id = request.POST['r_id'],
			stud_id = 1,
			response = request.POST['response'],
			timestamp = request.POST['timestamp'],
			mark_scored = request.POST['mark_scored'],
			answered = request.POST['answered'], 
		)
		obj.save()



	return render(request,'msat/home.html',context)


