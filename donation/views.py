from django.shortcuts import render
from django.shortcuts import redirect, render
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required
from donation.models import Donatee
from django.views.decorators.csrf import csrf_exempt
from donation.forms import OpenDonationForm

# Create your views here.
# Create your views here.
@login_required(login_url='/login/')
def show_donation(request):
    if request.method == 'POST':

        form = OpenDonationForm(request.POST)

        if form.is_valid():
            donatee = form.save()
            donatee.opener = request.user
            donatee.save()

            return redirect('donation:show_donation')

    else:
        form = OpenDonationForm()

    context = {
        'user' : request.user,
        'user_profile' : request.user.profile_pict_url,
        'form': form,
    }
    return render(request, "donation_page.html", context)

@login_required(login_url='/login/')
def show_donation_user(request):
    if request.method == 'POST':

            form = OpenDonationForm(request.POST)

            if form.is_valid():
                donatee = form.save()
                donatee.opener = request.user
                donatee.save()

                return redirect('donation:show_donation_user')

    else:
        form = OpenDonationForm()

    context = {
            'user' : request.user,
            'user_profile' : request.user.profile_pict_url,
            'form': form,
    }
    return render(request, "donation_page_user.html", context)

def show_json(request):
    data = Donatee.objects.filter(is_verified = True)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_admin(request):
    data = Donatee.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_user(request):
    data = Donatee.objects.filter(opener = request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def donation_detail(request, id):
    post_detail = Donatee.objects.get(pk = id)
    context = {
        'postdetail' : post_detail
    }
    return render(request, "donation_details.html", context)

def donate(request, id):
    if request.POST.get('action') == 'post':
        donatee = Donatee.objects.get(id=id)
        donatee.collectedFunds = donatee.collectedFunds + int(request.POST.get('amount'))
        donatee.save()
        return redirect('donation:show_donation')

@csrf_exempt
def donation_delete(request, id):
    Donatee.objects.filter(id=id).delete()
    return redirect('donation:show_donation_user')

@login_required(login_url='/login/')
def delete_by_admin(request, id):
    if request.user.is_admin:
        Donatee.objects.filter(id=id).delete()
        return JsonResponse({'status': 'Donatee is deleted successfully'})
    else:
        return JsonResponse({'status': 'Invalid deletion'}, status=403)

@login_required(login_url='/login/')
def change_status_donatee(request, id):
    if request.user.is_admin:
        donatee = Donatee.objects.get(id=id)
        donatee.is_verified = not donatee.is_verified
        donatee.save()
    else:
        return HttpResponse("Not allowed", status=403)
    return redirect('home:show_index')