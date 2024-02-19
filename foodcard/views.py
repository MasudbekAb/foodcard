from django.shortcuts import render
from .models import Categories, Receipt, Ingredients, Instructions

def main_page(request):
    category = Categories.objects.all()
    ingredients = Ingredients.objects.all()
    instructions = Instructions.objects.all()
    receipt = Receipt.objects.all()
    context = {
        "title": 'Main page',
        "Category": category,
        "Ingredients": ingredients,
        "Receipt": receipt
    }
    return render(request, 'foodcard/main_page.html', context)

def category_page(request, category_id):
    category = Categories.objects.all()
    receipt = Receipt.objects.filter(category=category_id)
    context = {
        "title": f"Category: {Categories.objects.get(id=category_id)}",
        'receipt': receipt,
    }

    return render(request, 'foodcard/category_page.html', context)

def receipt_detail(request, article_id):
    receipt = Receipt.objects.get(id=article_id)

    context = {
        "title": f"Receipt of {receipt.title}",
        "receipt": receipt
    }

    return render(request, 'foodcard/receipt_detail.html', context)


