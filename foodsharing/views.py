import datetime
from multiprocessing import context
from django.shortcuts import render, redirect
from foodsharing.models import Sharing
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required

# Create your views here.
# semua orang juga bisa baca
def show_location(request):
    data_post = Sharing.objects.order_by('-date')
    context = {
        'locationlist' : data_post
    }
    return render(request, "location_page.html", context)

def location_detail(request, id):
    location_detail = Sharing.objects.get(pk = id)
    context = {
        'locationdetail' : location_detail
    }
    return render(request, "location_detail.html", context)

# harus pas kondisi login
@login_required(login_url='home/login/')
@csrf_exempt
def add_location(request):
    if request.method == 'POST':
        location = request.POST.get('location')
        description = request.POST.get('description')
        img = request.POST.get('img')
        Sharing.objects.create(author=request.user, img = img, location = location, description=description, date=datetime.datetime.now())
        
        return redirect('foodsharing:show_location')

def show_json(request):
    data = Sharing.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def edit_add(request, id):
    edit = Sharing.objects.get(pk = id)
    context = {
        'edit' : edit
    }
    return render(request, "edit.html", context)

def edit_add_save(request, id):
	if request.method == "POST":
		x = Sharing.objects.get(pk = id)
		x.location = request.POST['location']
		x.description = request.POST['description']
		x.save()
		
		return redirect('foodsharing:show_location')

def delete(request, id):
    editing = Sharing.objects.get(pk=id)
    editing.delete()
    return redirect('foodsharing:show_location')