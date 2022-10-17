import datetime
from django.shortcuts import render, redirect
from blog.models import Post
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required

def show_post(request):
    data_post = Post.objects.order_by('-created_on')
    context = {
        'postlist' : data_post
    }
    return render(request, "post-page.html", context)

def post_detail(request, id):
    post_detail = Post.objects.get(pk = id)
    return render(request, "post-detail.html", post_detail)

# @csrf_exempt
# # @login_required(login_url='/login/')
# # dia login tapi balik ke homepage, gimana caranya biar dia abis login langsung di route lagi ke page
# def add_post(request):
#     if request.method == 'POST':
#         title = request.POST.get('title')
#         author = request.POST.get('author')
#         content = request.POST.get('content')

#         post = Post.objects.create(title=title, author=author, content=content, created_on=datetime.datetime.now())

#         result = {
#             'fields':{
#                 'title':post.title,
#                 'author':post.author,
#                 'content':post.content,
#                 'created_on':post.created_on,
#             },
#             'pk':post.pk
#         }

#         return JsonResponse(result)

def upload(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        Post.objects.create(title=title, author=request.user, content=content, created_on=datetime.datetime.now())

        return redirect('blog:show_post')

    return render(request, 'add-post.html')

def show_json(request):
    data = Post.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
