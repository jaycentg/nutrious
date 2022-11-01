import datetime
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
   
    context = {
        'locationlist' : data_post,
        'user_profile' : request.user.profile_pict_url,
    }
    
    if request.user.is_authenticated:
        context = {
        'locationlist' : data_post,
        'user_profile' : request.user.profile_pict_url,
        }
    
    return render(request, "location_page.html", context)

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

@login_required(login_url='home/login/')
@csrf_exempt
def edit_add(request, id):
    edit = Sharing.objects.get(pk = id)
    dic = {}
    dic['pk'] = edit.pk
    dic['img'] = edit.img
    dic['location'] = edit.location
    dic['description'] = edit.description
    # print("user", request.user, edit.author)
    if(request.user == edit.author):

        # print("aosdsodosd", dic)
        context = {
            'edit' : dic,
        }
        import json
        # return render(request, "location_page.html", context)
        return HttpResponse(json.dumps(dic))

@login_required(login_url='home/login/')
@csrf_exempt
def edit_add_save(request, id):
    if request.method == "POST":
        edit = Sharing.objects.get(pk = id)
        # user hanya bisa edit post sendiri
        if(request.user == edit.author):
            edit.location = request.POST['location']
            edit.description = request.POST['description']
            edit.img = request.POST['img']
            edit.update_date = datetime.datetime.now()
            edit.save()
    return redirect('foodsharing:show_location')
        
@login_required(login_url='home/login/')
@csrf_exempt
def delete(request, id):
    edit = Sharing.objects.get(pk=id)
    # user hanya bisa delete post sendiri
    if(request.user == edit.author):
        edit.delete()
    return redirect('foodsharing:show_location')