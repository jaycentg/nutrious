from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
             auth_login(request, user)
             return JsonResponse({
               "status": True,
               "message": "Successfully logged in!",
               "username": request.user.username,
               "is_admin": request.user.is_admin,
               "is_verified_user": request.user.is_verified_user,
               "nickname": request.user.nickname,
               "description": request.user.description,
               "profile_pict_url": request.user.profile_pict_url
             }, status=200)
        else:
            return JsonResponse({
               "status": False,
               "message": "Failed to login, account disabled."
            }, status=401)
    else:
        return JsonResponse({
           "status": False,
           "message": "Failed to login, check your email/password."
         }, status=401)