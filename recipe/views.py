import datetime
from django.shortcuts import render, redirect, get_object_or_404
from recipe.models import FoodRecipe
from recipe.forms import CreateRecipe
from home.models import AppUser
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required

@csrf_exempt
def show_recipe(request):
    data_recipe = FoodRecipe.objects.order_by('-created_on')
    context = {
        'recipe_list' : data_recipe
    }
    return render(request, "recipes.html", context)

def add_recipe(request):
    if request.method == 'POST':
        food_name = request.POST.get('food_name')
        ingredients = request.POST.get('ingredients')
        method = request.POST.get('method')
    
        new_recipe = FoodRecipe(food_name=food_name, ingredients=ingredients, method=method, author=request.user, created_on=datetime.datetime.now())
        new_recipe.save()

        return HttpResponse(b"CREATED", status=201)

def show_json(request):
    data = FoodRecipe.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
