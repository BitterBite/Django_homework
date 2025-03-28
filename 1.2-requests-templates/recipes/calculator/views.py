from django.shortcuts import render
from django.http import Http404

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


def recipe(request, dish_name):
    if dish_name not in DATA:
        raise Http404(f"Рецепт '{dish_name}' не найден")

    servings = int(request.GET.get('servings', 1))

    recipe = {
        ingredient: amount * servings
        for ingredient, amount in DATA[dish_name].items()
    }

    context = {
        'recipe': recipe,
        'dish_name': dish_name,
        'servings': servings,
        'available_recipes': list(DATA.keys())  # Список доступных рецептов
    }

    return render(request, 'calculator/index.html', context)
