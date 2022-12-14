from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from home.forms import *
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required
from home.models import *
from donation.models import Donatee
from django.views.decorators.csrf import csrf_exempt

DEF_PICT_URL = 'https://uxwing.com/wp-content/themes/uxwing/download/peoples-avatars/no-profile-picture-icon.png'

# Create your views here.
def register(request):
    form = AppUserCreationForm()
    if request.method == 'POST':
        form = AppUserCreationForm(request.POST)
        if form.is_valid():
            if not form.instance.profile_pict_url:
                form.instance.profile_pict_url = DEF_PICT_URL
            form.save()
            return redirect('home:login')
    
    context = {'form': form}
    return render(request, 'registration.html', context)

def show_index(request):
    if request.user.is_authenticated:
        # Jika user merupakan admin
        if request.user.is_admin:
            context = {}
            context['users'] = AppUser.objects.filter(is_admin=False, is_superuser=False)
            context['donatees'] = Donatee.objects.all()
            context['username'] = request.user.username
            context['profile_url'] = request.user.profile_pict_url
            return render(request, 'index_admin.html', context)
        # Jika user cuma user biasa
        else:
            form = MessageForm()
            context = {}
            context['username'] = request.user.username
            context['nickname'] = request.user.nickname
            context['profile_url'] = request.user.profile_pict_url
            context['is_verified'] = request.user.is_verified_user
            context['form'] = form
            return render(request, 'index_auth.html', context)
    else:
        return render(request, 'index.html')

@login_required(login_url='/login/')
@csrf_exempt
def add_message(request):
    if request.method == 'POST':
        user = request.user
        message = request.POST.get('message')
        Message.objects.create(user=user, message=message)
        return JsonResponse({'status':'Message is sent successfully'})
    else:
        return JsonResponse({'status': 'Invalid request'}, status=400)

@login_required(login_url='/login/')
@csrf_exempt
def show_profile(request):
    context = {}
    context['username'] = request.user.username
    context['nickname'] = request.user.nickname
    context['profile_url'] = request.user.profile_pict_url
    context['description'] = request.user.description
    if request.user.is_verified_user:
        context['status'] = 'Verified'
    else:
        context['status'] = 'Not Verified'
    return render(request, 'profile.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home:show_index')
        else:
            messages.info(request, 'Username or password is wrong')
    return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    return redirect('home:login')

@login_required(login_url='/login/')
def json_user(request):
    data = AppUser.objects.filter(is_admin=False, is_superuser=False)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required(login_url='/login/')
def change_status_user(request, id):
    if request.user.is_admin:
        user = AppUser.objects.get(id=id)
        user.is_verified_user = not user.is_verified_user
        user.save()
    else:
        return HttpResponse("Not allowed", status=403)
    return redirect('home:show_index')

@login_required(login_url='/login/')
def delete_user(request, id):
    if request.user.is_admin:
        user = AppUser.objects.get(id=id)
        user.delete()
        return JsonResponse({'status': 'User is deleted successfully'})
    else:
        return JsonResponse({'status': 'Invalid deletion'}, status=403)

@login_required(login_url='/login/')
def show_json_message(request):
    data = Message.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required(login_url='/login/')
def delete_message(request, id):
    if request.user.is_admin:
        msg = Message.objects.get(id=id)
        msg.delete()
        return JsonResponse({'status': 'Message is deleted successfully'})
    else:
        return JsonResponse({'status': 'Invalid deletion'}, status=403)

@login_required(login_url='/login/')
def show_json_message_with_sender(request):
    list_of_messages = []
    messages = Message.objects.all()
    for message in messages:
        msg_instance = {}
        msg_instance["pk"] = message.id
        msg_instance["sender"] = message.user.username
        msg_instance["message"] = message.message
        msg_instance["time"] = message.time_sent
        list_of_messages.append(msg_instance)
    return JsonResponse({'data': list_of_messages})