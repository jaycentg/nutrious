
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from calorietracker.models import Calorie
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
@login_required(login_url='/login/')
def show_caloriepage(request):
	data = Calorie.objects.order_by('-date')
	if request.user.is_authenticated:
		context = {
			'user' : request.user,
			'nickname' : request.user.nickname,
			'user_profile' : request.user.profile_pict_url,
			'data' : data,
	}
	else:
		context = {
			'user' : request.user,
			'data' : data,
		}
	return render(request, 'calorietracker.html',context)

@login_required(login_url='/home/login/')
@csrf_exempt
def add_calorie(request):
	if request.method == "POST":
		calorie = request.POST.get("calorie")
		description = request.POST.get("description")
		category = request.POST.get("category")
		date= request.POST.get('date')
		time= request.POST.get('time')
		Calorie.objects.create(time = time,category = category,is_increasing = True, date =date,calorie= calorie, description = description, user=request.user)
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
		date= request.POST.get('date')
		time= request.POST.get('time')
		Calorie.objects.create(time = time,category = category,is_increasing = False, date =date,calorie= calorie, description = description, user=request.user)

		return HttpResponse()
	else:
		return redirect('calorietracker:show_caloriepage')

def show_json(request):
    data =Calorie.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")   

def edit_add(request, id):
    edit = Calorie.objects.get(pk = id)
    context = {
        'edit' : edit,
		'user_profile' : request.user.profile_pict_url,
    }
    return render(request, "edit.html", context)
def edit_reduce(request, id):
    edit = Calorie.objects.get(pk = id)
    context = {
        'edit' : edit,
		'user_profile' : request.user.profile_pict_url,
    }
    return render(request, "edit_reduce.html", context)
def edit_reduce_save(request, id):
	if request.method == "POST":
		x = Calorie.objects.get(pk = id)
		x.calorie = request.POST['calorie']
		x.description = request.POST['description']
		
		x.save()
		
		return redirect('calorietracker:show_caloriepage')
def edit_add_save(request, id):
	if request.method == "POST":
		x = Calorie.objects.get(pk = id)
		x.calorie = request.POST['calorie']
		x.description = request.POST['description']
		x.category = request.POST['category']
		x.save()
		
		return redirect('calorietracker:show_caloriepage')
def delete(request, id):
	edit = Calorie.objects.get(pk = id)
	edit.delete()
	return redirect('calorietracker:show_caloriepage')


@csrf_exempt
def calorief(request):
	if (request.method == 'POST'):
		calorie =int(request.POST.get("calorie")) 
		description = request.POST.get("description")
		category = request.POST.get("category")
		is_increasing_ = request.POST.get("is_increasing")
		date = request.POST.get("date")
		time =  request.POST.get("time")
		if(is_increasing_ =="false"):
			is_increasing = False
		else:
			is_increasing = True
		user = request.user
		obj_baru = Calorie(user = user, calorie=calorie, description = description, category = category,is_increasing = is_increasing, time=time, date=date)
		obj_baru.save()
		return JsonResponse({'status': 'berhasil dibuka'}, status=200)

@login_required(login_url='/login/')
def show_jsonf(request):
	list_of_calorie = []
	calories= Calorie.objects.filter(user=request.user)
	for calorie in calories:
		calorie_instance = {}
		calorie_instance["pk"] = calorie.id
		calorie_instance["calorie"] = calorie.calorie
		calorie_instance["description"] = calorie.description
		calorie_instance["category"] = calorie.category
		calorie_instance["is_increasing"] = calorie.is_increasing
		calorie_instance["date"] = calorie.date
		calorie_instance["time"] = calorie.time 
		list_of_calorie.append(calorie_instance)
	return JsonResponse({"data": list_of_calorie})

@csrf_exempt
def deletef(request):
    if (request.method == 'POST'):
        id = request.POST.get('id')
        Calorie.objects.get(pk=int(id)).delete()
        return JsonResponse({'status': 'berhasil ditutup'}, status=200)
@csrf_exempt
def deleteAllf(request):
    if (request.method == 'POST'):
        Calorie.objects.all().delete()
        return JsonResponse({'status': 'berhasil ditutup'}, status=200)

@csrf_exempt
def edit_reduce_savef(request):
	if (request.method == 'POST'):
		id = request.POST.get('id')
		x = Calorie.objects.get(pk=int(id))
		x.calorie = int(request.POST.get("calorie")) 
		x.description = request.POST.get("description")
		x.save()
		return JsonResponse({"data": "success"})

@csrf_exempt
def edit_add_savef(request):
	if (request.method == 'POST'):
		id = request.POST.get('id')
		x = Calorie.objects.get(pk=int(id))
		x.calorie = int(request.POST.get("calorie")) 
		x.description = request.POST.get("description")
		x.category = request.POST.get("category")
		x.save()
		return JsonResponse({"data": "success"})

