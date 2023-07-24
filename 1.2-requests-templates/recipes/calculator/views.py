from django.shortcuts import render

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

def recipe(request, recipe):
    if recipe in DATA:
        servings = request.GET.get('servings', 1)
        data = DATA[recipe].copy()

        for ingredient, amount in data.items():
            data[ingredient] = amount * int(servings)

        context = {
            'recipe':
               data
        }
    
        return render(request, 'calculator/index.html', context)
    else:
        return render(request, 'calculator/index.html')