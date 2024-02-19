from django.contrib import admin
from .models import Categories, Receipt, Ingredients, Instructions

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(Receipt)
class ReceiptAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'cooking_time')
    list_filter = ('category', 'cooking_time')
    search_fields = ('title', 'description')

@admin.register(Ingredients)
class IngredientsAdmin(admin.ModelAdmin):
    list_display = ('name', 'receipt')
    list_filter = ('receipt',)
    search_fields = ('name',)

@admin.register(Instructions)
class InstructionsAdmin(admin.ModelAdmin):
    list_display = ('name', 'receipt')
    list_filter = ('receipt',)
    search_fields = ('name',)
