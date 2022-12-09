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
    }
    
    if request.user.is_authenticated:
        context = {
        'locationlist' : data_post,
        'user_profile' : request.user.profile_pict_url,
        'nickname': request.user.nickname,
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
        now = datetime.datetime.now()
        date = now.strftime("%d-%m-%Y, %H:%M:%S")
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
            edit.update_date = datetime.datetime.now().strftime("%d-%m-%Y, %H:%M:%S")
            
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

@csrf_exempt
def foodsharingf(request):
    if (request.method == "POST"):
        location = request.POST.get('location')
        description = request.POST.get('description')
        img = request.POST.get('img')
        now = datetime.datetime.now()
        date = now.strftime("%d-%m-%Y, %H:%M:%S")
        update_date = date
        obj = Sharing(update_date = update_date, author=request.user, date = date, img = img, location = location, description=description)
        obj.save()
        return JsonResponse({'status': 'berhasil dibuka'}, status= 200)

@login_required(login_url='/login/')
def show_jsonf(request):
    list_foodsharing = []
    foodsharings = Sharing.objects.all()
    for foodsharing in foodsharings:
        foodsharing_instance = {}
        foodsharing_instance['pk'] = foodsharing.id
        foodsharing_instance['author'] = foodsharing.getAuthorName()
        foodsharing_instance['location'] = foodsharing.location 
        foodsharing_instance['description'] = foodsharing.description
        foodsharing_instance['img'] = foodsharing.img
        foodsharing_instance['date'] = foodsharing.date
        foodsharing_instance['updateDate'] = foodsharing.update_date
    return JsonResponse({'data':list_foodsharing})



@csrf_exempt
def deletef(request):
    if (request.method == 'POST'):
        id = request.POST.get('id')
        if  (request.user == id.author):
            Sharing.objects.get(pk=int(id)).delete()
            return JsonResponse({'status':'berhasil delete'}, status = 200)

@csrf_exempt
def edit_add_savef(request):
    if (request.method == 'POST'):
        id = request.POST.get('id')
        if  (request.user == id.author):
            x = Sharing.objects.get(pk=int(id))
            x.location = request.POST.get('location')
            x.description = request.POST.get('description')
            x.img = request.POST.get('img')
            x.update_date =  datetime.datetime.now().strftime("%d-%m-%Y, %H:%M:%S")
            x.save()
            return JsonResponse({'data':'edit success'})

@login_required(login_url='/login')
def show_json_by_user(request):
    list_foodsharings = []
    foodsharings = Sharing.objects.filter(opener = request.user)
    for foodsharing in foodsharings:
        foodsharing_instance = {}
        foodsharing_instance['pk']= foodsharing.id
        foodsharing_instance['author']= foodsharing.getAuthorName()
        foodsharing_instance['location'] = foodsharing.location 
        foodsharing_instance['description'] = foodsharing.description
        foodsharing_instance['img'] = foodsharing.img
        foodsharing_instance['date'] = foodsharing.date
        foodsharing_instance['updateDate'] = foodsharing.update_date
        list_foodsharings.append(foodsharing_instance)
    return JsonResponse({'data':list_foodsharings})