import datetime

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.core import serializers
from django.urls import reverse

from recipe.models import FoodRecipe
from recipe.forms import CreateRecipe
from home.models import AppUser

@csrf_exempt
def show_recipe(request):
    data_recipe = FoodRecipe.objects.order_by('-created_on')
    context = {
        'recipe_list' : data_recipe
    }
    return render(request, "recipes.html", context)


def show_json(request):
    data = FoodRecipe.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


def add_recipe(request):
    if request.method == 'POST':
        food_name = request.POST.get('food_name')
        ingredients = request.POST.get('ingredients').replace("\n", "</li> <li>" )
        method = request.POST.get('method').replace("\n", "</li> <li>" )
        date = datetime.datetime.now()
        formatted_date = formatted_date = date.strftime("%d") + " " + date.strftime("%B") + " " + date.strftime("%Y")

        new_recipe = FoodRecipe(food_name=food_name, ingredients=ingredients, method=method, author=request.user, author_name=request.user.username, created_on=date, formatted_date=formatted_date)
        new_recipe.save()

        return HttpResponse(b"CREATED", status=201)


@csrf_exempt
def delete(request, id):
    task = FoodRecipe.objects.get(pk=id)
    if (task.user == request.user):
        FoodRecipe.objects.filter(pk=id).delete()
        return HttpResponseRedirect(reverse('recipe:show_recipe'))