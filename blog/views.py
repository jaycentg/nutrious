import datetime
from django.shortcuts import render, redirect, get_object_or_404
from blog.models import Post
from home.models import AppUser
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required

@csrf_exempt
def show_post(request):
    
    data_post = Post.objects.order_by('-created_on')
    postarr = []
    for user in data_post:
        splitArr = user.tag.split(" ")
        for i in splitArr:
            if (i not in postarr):
                postarr.append(i)

    context = {
        'postlist' : data_post,
        'taglist' : postarr
    }
    if request.user.is_authenticated:
        return render(request, "post-page-auth.html", context)
    else:
        return render(request, "post-page-unauth.html", context)


    

def post_detail(request):
    post_detail = Post.objects.all()
    context = {
        'postdetail' : post_detail,
    }
    return render(request, "post-detail.html", context)


# ini harus login juga
@login_required(login_url='/login/')
def upload(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        tag = request.POST.get('tag')
        post = Post.objects.create(title=title, author=request.user.nickname, content=content, created_on=datetime.datetime.now(), upvote=0, downvote=0, vote_state=2, tag=tag)

        return redirect('blog:show_post')

    return render(request, 'add-post.html')

def show_json(request):
    data = Post.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_tag(request, tag):
    query = Post.objects.filter(
        Q(tag__icontains=tag)
    )
    return HttpResponse(serializers.serialize("json", query), content_type="application/json")

def show_json_by_id(request, id):
    data = Post.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

# login dulu
@csrf_exempt
@login_required(login_url='/login/')
def addUpvote(request, id):
    if request.method == 'PATCH':

        post_detail = get_object_or_404(Post, pk = id)
        voted = False
        downvoted = False
        upvoted = False

        for post in request.user.post.all():         
            # cari dia udah pernah vote atau belum post tersebut
            if (post.pk == post_detail.pk):
                voted = True
                # kalo user udah downvoted postnya sebelumnya
                if(post.vote_state == 1):
                    downvoted = True
                    upvoted = False
                    break
                # kalo user udah upvoted postnya sebelumnya
                elif(post.vote_state == 0):
                    upvoted = True
                    downvoted = False
                    break
                # kalau state nya 2 berarti belum di vote lagi walaupun udah ada
                else:
                    voted = False
                    break
            # kalo belum pernah vote post tersebut
            else:
                voted = False

        # jika pernah vote
        if (voted):
            # pernah downvote terus mencet upvote
            if (downvoted):
                post_detail.downvote = post_detail.downvote - 1
                post_detail.upvote = post_detail.upvote + 1
                post_detail.vote_state = 0 #nyimpen kalo dia jadi upvote
                post_detail.save()

            # pernah upvote terus upvote lagi
            elif (upvoted):
                post_detail.upvote = post_detail.upvote - 1
                post_detail.vote_state = 2
                post_detail.save()
                request.user.post.remove(post_detail)
                request.user.save()

        else:
            post_detail.upvote = post_detail.upvote + 1
            post_detail.vote_state = 0
            post_detail.save()
            request.user.post.add(post_detail)
            request.user.save()

        result = {
            'pk': post_detail.pk,
            'fields':{
                'title': post_detail.title,
                'author': post_detail.author,
                'content': post_detail.content,
                'created_on': post_detail.created_on,
                'upvote': post_detail.upvote,
                'downvote': post_detail.downvote,
                'tag': post_detail.tag,
                }
        }
        
    return JsonResponse(result)

@csrf_exempt
@login_required(login_url='/login/')
def addDownvote(request, id):
    if request.method == 'PATCH':

        post_detail = get_object_or_404(Post, pk = id)
        voted = False
        downvoted = False
        upvoted = False

        for post in request.user.post.all():
            # cari dia udah pernah vote atau belum post tersebut
            if (post.pk == post_detail.pk):
                voted = True
                # kalo user udah downvoted postnya sebelumnya
                if(post.vote_state == 1):
                    downvoted = True
                    upvoted = False
                    break
                # kalo user udah upvoted postnya sebelumnya
                elif(post.vote_state == 0):
                    upvoted = True
                    downvoted = False
                    break
                # kalau state nya 2 berarti belum di vote lagi walaupun udah ada
                else:
                    voted = False
                    break
            # kalo belum pernah vote post tersebut
            else:
                voted = False

        # jika pernah vote
        if (voted):
            # pernah downvote terus mencet downvote
            if (downvoted):
                request.user.post.remove(post_detail)
                post_detail.downvote = post_detail.downvote - 1
                post_detail.vote_state = 2
                post_detail.save()
                request.user.post.add(post_detail)
                request.user.save()
                
            # pernah upvote terus downvote
            elif (upvoted):
                request.user.post.remove(post_detail)
                post_detail.upvote = post_detail.upvote - 1
                post_detail.downvote = post_detail.downvote + 1
                post_detail.vote_state = 1 #nyimpen kalo dia jadi downvote
                post_detail.save()
                request.user.post.add(post_detail)
                request.user.save()
                
        else:
            post_detail.downvote = post_detail.downvote + 1
            post_detail.vote_state = 1
            post_detail.save()
            request.user.post.add(post_detail)
            request.user.save()

        result = {
            'pk': post_detail.pk,
            'fields':{
                'title': post_detail.title,
                'author': post_detail.author,
                'content': post_detail.content,
                'created_on': post_detail.created_on,
                'upvote': post_detail.upvote,
                'downvote': post_detail.downvote,
                'tag': post_detail.tag,
            }
        }
        
    return JsonResponse(result)

@csrf_exempt
def add_post(request):
    if (request.method == 'POST'):
        title = request.POST.get('title')
        content = request.POST.get('content')
        tag = (request.POST.get('tag'))
        post = Post(title=title, author=request.user.nickname, content=content, created_on=datetime.datetime.now(), upvote=0, downvote=0, vote_state=2, tag=tag)
        post.save()

        return JsonResponse({'status': 'berhasil dibuka'}, status=200)


@csrf_exempt
def show_post_by_tag(request, tag):
    list_of_posts = []
    query = Post.objects.filter(
        Q(tag__icontains=tag)
    )
    for post_detail in query:
        result = {
            'pk': post_detail.pk,
            'fields':{
                'title': post_detail.title,
                'author': post_detail.author,
                'content': post_detail.content,
                'created_on': post_detail.created_on,
                'upvote': post_detail.upvote,
                'downvote': post_detail.downvote,
                'vote_state': post_detail.vote_state,
                'tag': post_detail.tag,
            }
        }
        list_of_posts.append(result)
    return JsonResponse({"data": list_of_posts})
    # return JsonResponse(query)
