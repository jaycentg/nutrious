from django.shortcuts import render
from django.shortcuts import redirect, render
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required
from donation.models import Donatee

# Create your views here.
@login_required(login_url='/home/login/')
def show_donation(request):
    data_post = Donatee.objects.filter(is_verified = True)
    context = {
        'user' : request.user,
        'data_post' : data_post
    }
    return render(request, "donation_page.html", context)

@login_required(login_url='/home/login/')
def create_donation(request):
    if request.method == 'POST':
            title = request.POST.get('title')
            description = request.POST.get('description')
            amountNeeded = request.POST.get('amountNeeded')

            Donatee.objects.create(title=title, author=request.user, description=description, amountNeeded=amountNeeded)

            return redirect('donation:show_donation')

    context = {
            'user' : request.user,
    }
    return render(request, 'add_donation.html', context)

def show_json(request):
    data = Donatee.objects.filter(is_verified = True)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def donation_detail(request, id):
    post_detail = Donatee.objects.get(pk = id)
    context = {
        'postdetail' : post_detail
    }
    return render(request, "donation_details.html", context)

def donate(request, id):
    if request.method == 'POST':
        donatee = Donatee.objects.get(id=id)
        donatee.collectedFunds = donatee.collectedFunds + int(request.POST.get('amount'))
        donatee.save()
        return redirect('donation:show_donation')