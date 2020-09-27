import nested_admin

from django.contrib import admin

from .models import Ingredient, Method, Section, Recipe, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
    exclude = ['slug']


class IngredientAdmin(admin.ModelAdmin):
    list_display = ['title', 'amount', 'measure']
    exclude = ['slug']
    radio_fields = {'measure': admin.HORIZONTAL}


class MethodAdmin(admin.ModelAdmin):
    list_display = ['description']


class SectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'ingredient', 'method']


class IngredientInline(nested_admin.NestedStackedInline):
    model = Ingredient
    radio_fields = {'measure': admin.HORIZONTAL}
    extra = 0


class MethodInline(nested_admin.NestedStackedInline):
    model = Method
    extra = 0


class SectionInline(nested_admin.NestedStackedInline):
    model = Section
    inlines = [IngredientInline, MethodInline]
    extra = 0


class RecipeAdmin(nested_admin.NestedModelAdmin):
    inlines = [SectionInline]
    exclude = ['slug']
    search_fields = ('title',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Recipe, RecipeAdmin)
