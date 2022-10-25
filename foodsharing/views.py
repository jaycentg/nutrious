import datetime
from django.shortcuts import render, redirect
from foodsharing.models import Post
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required

# Create your views here.
# semua orang juga bisa baca
def show_location(request):
    data_post = Post.objects.order_by('-date')
    context = {
        'postlist' : data_post
    }
    return render(request, "location_page.html", context)

def post_detail(request, id):
    post_detail = Post.objects.get(pk = id)
    context = {
        'postdetail' : post_detail
    }
    return render(request, "location_detail.html", context)

# harus pas kondisi login
@login_required(login_url='/home/login/')
def add_location(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        location = request.POST.get('location')

        Post.objects.create(author=request.user, location = location, content=content, date=datetime.datetime.now())
        return redirect('foodsharing:show_location')

    return render(request, 'add_location.html')

def show_json(request):
    data = Post.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")