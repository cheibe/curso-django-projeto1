from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse, Http404
from utils.recipes.factory import make_recipe
from recipes.models import Recipe
from django.db.models import Q
from django.core.paginator import Paginator 

def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')

    current_page = request.GET.get('page', 1)
    paginator = Paginator(recipes, 9)
    page_object = paginator.get_page(current_page)

    return render(request, 'recipes/pages/home.html', context={
        'recipes': page_object,
    })

def recipe(request, id):
    recipe = get_object_or_404(Recipe, pk=id, is_published=True)

    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': recipe,
        'is_detail_page': True,
    })

def category(request, category_id):

    recipes = get_list_or_404(
        Recipe.objects.filter(
            category__id=category_id,
            is_published=True,
        ).order_by('-id')
    )

    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
        'title': f'{recipes[0].category.name}  - CATEGORY |'
    })

def search(request):
    search_term = request.GET.get('search', '').strip()
    if not search_term:
        raise Http404()
    
    recipes = Recipe.objects.filter(
        Q(
            Q(title__icontains=search_term) | 
            Q(description__icontains=search_term),
        ), is_published=True
    ).order_by('-id')
    
    return render(request, 'recipes/pages/search.html', {
        'page_title': f'Search for "{search_term}" | ',
        'searche_term': search_term,
        'recipes': recipes,
        })