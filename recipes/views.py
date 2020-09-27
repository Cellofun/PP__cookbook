import json

from django.db.models import Q
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.base import ContextMixin

from .models import Category, Recipe, Ingredient


class PaginatorMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super(PaginatorMixin, self).get_context_data(**kwargs)

        if not context.get('is_paginated', False):
            return context

        paginator = context.get('paginator')
        num_pages = paginator.num_pages
        current_page = context.get('page_obj')
        page_no = current_page.number

        if num_pages <= 11 or page_no <= 6:
            pages = [x for x in range(1, min(num_pages + 1, 12))]
        elif page_no > num_pages - 6:
            pages = [x for x in range(num_pages - 10, num_pages + 1)]
        else:
            pages = [x for x in range(page_no - 5, page_no + 6)]

        context.update({'pages': pages})
        return context


class RecipeListView(PaginatorMixin, ListView):
    model = Recipe
    paginate_by = 9
    template_name = 'recipes/recipe_list.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = Recipe.objects.filter(
                Q(title__icontains=query) | Q(description__icontains=query)
            )
        else:
            object_list = Recipe.objects.all()
        return object_list

    def get_context_data(self, **kwargs):
        context = super(RecipeListView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all().order_by('title')
        return context


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipes/recipe_detail.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super(RecipeDetailView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all().order_by('title')
        return context


class CategoryListView(PaginatorMixin, ListView):
    model = Category
    paginate_by = 9
    template_name = 'recipes/category_list.html'

    def get_queryset(self):
        object_list = Recipe.objects.filter(category__slug=self.kwargs['slug'])
        return object_list

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all().order_by('title')
        context['category'] = Category.objects.filter(slug=self.kwargs['slug']).first()
        return context


class IngredientListView(PaginatorMixin, ListView):
    model = Ingredient
    paginate_by = 9
    template_name = 'recipes/ingredient_list.html'

    def get_queryset(self):
        object_list = Recipe.objects.filter(section__ingredient__slug=self.kwargs['slug']).distinct()
        return object_list

    def get_context_data(self, **kwargs):
        context = super(IngredientListView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all().order_by('title')
        context['ingredient'] = Ingredient.objects.filter(slug=self.kwargs['slug']).first()
        return context


def autocomplete(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        recipes = Recipe.objects.filter(title__icontains=q)
        results = []
        for recipe in recipes:
            recipe_json = {
                'title': recipe.title,
                'slug': recipe.slug,
                'description': recipe.description
            }
            results.append(recipe_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)
