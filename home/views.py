from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import AppUserCreationForm
from django.contrib import messages
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required
from .models import AppUser

# Create your views here.
class Register(CreateView):
    form_class = AppUserCreationForm
    success_url = reverse_lazy('home:login')
    template_name = 'registration.html'

def show_index(request):
    if request.user.is_authenticated:
        # Jika user merupakan admin
        if request.user.is_admin:
            context = {}
            context['users'] = AppUser.objects.filter(is_admin=False)
            context['username'] = request.user.username
            context['profile_url'] = request.user.profile_pict_url
            return render(request, 'index_admin.html', context)
        # Jika user cuma user biasa
        else:
            context = {}
            context['username'] = request.user.username
            context['nickname'] = request.user.nickname
            context['profile_url'] = request.user.profile_pict_url
            context['is_verified'] = request.user.is_verified_user
            return render(request, 'index_auth.html', context)
    else:
        return render(request, 'index.html')

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
    data = AppUser.objects.all()
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
    else:
        return HttpResponse("Not allowed", status=403)
    return redirect('home:show_index')