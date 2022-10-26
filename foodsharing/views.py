import datetime
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
@login_required(login_url='/login/')
@csrf_exempt
def add_location(request):
    if request.method == 'POST':
        # title = request.POST.get('title')
        description = request.POST.get('description')
        location = request.POST.get('location')

        Sharing.objects.create(author=request.user, location = location, description=description, date=datetime.datetime.now())
        return redirect('foodsharing:show_location')

    # return render(request, 'add_location.html')

def show_json(request):
    data = Sharing.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")