# from utils.recipes.factory import make_recipe
from django.shortcuts import get_list_or_404, render

from .models import Recipe


# Create your views here.
def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')  #Recipe.objects.all()

    return render(request, 'recipes/pages/home.html', context= {
        'recipes': recipes
    })

def category(request, category_id):
    # # filter objects by category // category__id = foreign key
    # recipes = Recipe.objects.filter(
    #     category__id=category_id,
    #     is_published=True
    # )
    # if not recipes:
    #     raise Http404('Not Found =(')

    recipes = get_list_or_404(
        Recipe.objects.filter(
            category__id=category_id,
            is_published=True
        ).order_by('-id')
    )

    return render(request, 'recipes/pages/category.html', context= {
        'recipes': recipes,
        'title': f'{recipes[0].category.name} - Category | '
    })

def recipes(request, id):
    # recipe = Recipe.objects.get(id=id)
    recipe = Recipe.objects.filter(
        id=id,
        is_published=True
    ).order_by('-id').first()
    
    return render(request, 'recipes/pages/recipes-view.html', context={
        'recipe': recipe,
        'is_detail_page': True,
    })

