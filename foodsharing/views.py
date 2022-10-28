import datetime, validators
from multiprocessing import context
from django.shortcuts import render, redirect
from foodsharing.models import Sharing
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.contrib import messages

import timeago
# Create your views here.
# semua orang juga bisa baca
def show_location(request):
    data_post = Sharing.objects.order_by('-date')

    for i in data_post:
        print(i)

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
        date=datetime.datetime.now()
        update_date = date
        Sharing.objects.create(update_date = update_date, author=request.user, date = date, img = img, location = location, description=description)
        
        return redirect('foodsharing:show_location')

def show_json(request):
    data = Sharing.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def edit_add(request, id):
    edit = Sharing.objects.get(pk = id)
    dic = {}
    dic['pk'] = edit.pk
    dic['img'] = edit.img
    dic['location'] = edit.location
    dic['description'] = edit.description
    print("aosdsodosd", dic)
    context = {
        'edit' : dic
    }
    import json
    # return render(request, "location_page.html", context)
    return HttpResponse(json.dumps(dic))


def edit_add_save(request, id):
    if request.method == "POST":
        x = Sharing.objects.get(pk = id)
        x.location = request.POST['location']
        x.description = request.POST['description']
        x.img = request.POST['img']
        x.date = datetime.datetime.now()
        x.save()
    return redirect('foodsharing:show_location')
        

def delete(request, id):
    editing = Sharing.objects.get(pk=id)
    editing.delete()
    return redirect('foodsharing:show_location')