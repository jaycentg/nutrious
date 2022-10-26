
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core import serializers
from calorietracker.models import Calorie
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import datetime
def show_caloriepage(request):
	
	context = {
    	'user' : request.user,
	}
	return render(request, 'calorietracker.html',context)

@login_required(login_url='/home/login/')
@csrf_exempt
def add_calorie(request):
	if request.method == "POST":
		calorie = request.POST.get("calorie")
		description = request.POST.get("description")
		category = request.POST.get("category")
		Calorie.objects.create(category = category,is_increasing = True, date = datetime.datetime.now(),calorie= calorie, description = description, user=request.user)
		return HttpResponse()
	else:
		return redirect('calorietracker:show_caloriepage')

@login_required(login_url='/home/login/')
@csrf_exempt
def reduce_calorie(request):
	if request.method == "POST":
		calorie = request.POST.get("calorie")
		description = request.POST.get("description")
		category = request.POST.get("category")
		Calorie.objects.create(category = category,is_increasing = False, date = datetime.datetime.now(), calorie = calorie, description = description, user=request.user)
		return HttpResponse()
	else:
		return redirect('calorietracker:show_caloriepage')

def show_json(request):
    data =Calorie.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")   

def edit(request, id):
    edit = Calorie.objects.get(pk = id)
    context = {
        'edit' : edit
    }
    return render(request, "edit.html", context)