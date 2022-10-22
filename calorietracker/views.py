from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from calorietracker.models import CalorieTracker
from calorietracker.forms import Form
from django.urls import reverse
from django.core import serializers
# Create your views here.
def show_caloriepage(request):
    data = CalorieTracker.objects.filter(user = request.user.id).only('calorie')

    
    total = 0
    for i in data:
        total+=i
    context = {
        'totalCalories' : total,
        'data': data,
         'user':request.user.id,
    }
    return render(request, "calorietracker.html", context)

def add_calorie(request):
    if request.method == "POST":
        calorie = request.POST.get("calorie")
        description = request.POST.get("description")
        
        CalorieTracker.objects.create(calorie = calorie, description = description, user=request.user)
        return HttpResponse()
    else:
        return redirect('calorietracker:show_caloriepage')
def show_json(request):
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")   

