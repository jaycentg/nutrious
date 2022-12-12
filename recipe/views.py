import datetime
import json

from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from recipe.models import FoodRecipe


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
        ingredients = request.POST.get('ingredients').strip().replace("\n", "</li> <li>" )
        method = request.POST.get('method').strip().replace("\n", "</li> <li>" )
        date = datetime.datetime.now()
        formatted_date = formatted_date = date.strftime("%d") + " " + date.strftime("%B") + " " + date.strftime("%Y")

        new_recipe = FoodRecipe(food_name=food_name, ingredients=ingredients, method=method, author=request.user, author_name=request.user.username, created_on=date, formatted_date=formatted_date)
        new_recipe.save()

        return HttpResponse(b"CREATED", status=201)


@csrf_exempt
def delete(request, id):
    food = FoodRecipe.objects.get(pk=id)
    if(request.user == food.author):
        food.delete()
    return redirect('recipe:show_recipe')

@csrf_exempt
def add_recipe_flutter(request):
    if request.method == 'POST':
        food_name = request.POST.get('food_name')
        ingredients = request.POST.get('ingredients').strip().replace("\n", "</li> <li>" )
        method = request.POST.get('method').strip().replace("\n", "</li> <li>" )
        date = datetime.datetime.now()
        formatted_date = date.strftime("%d") + " " + date.strftime("%B") + " " + date.strftime("%Y")

        new_recipe = FoodRecipe(food_name=food_name, ingredients=ingredients, method=method, author=request.user, author_name=request.user.username, created_on=date, formatted_date=formatted_date)
        new_recipe.save()

        data = {"succesed"}

        return JsonResponse(json.loads(data), safe=False)