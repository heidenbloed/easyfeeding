from django.shortcuts import render
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .serializers import RecipeNameSerializer, RecipeFullSerializer, IngredientNameSerializer, IngredientFullSerializer, UnitSerializer, IngredientCategorySerializer, QuantifiedIngredientSerializer, LabelSerializer
from .models import Recipe, Ingredient, QuantifiedIngredient, IngredientCategory, Unit, Label
from .filters import RecipeFilter


class RecipeView(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = RecipeFilter
    search_fields = ['name']
    ordering_fields = ['name', 'preparation_time']
    ordering = ['name']

    def get_serializer_class(self):
        if self.action == 'list':
            return RecipeNameSerializer
        else:
            return RecipeFullSerializer


class QuantifiedIngredientView(viewsets.ModelViewSet):
    serializer_class = QuantifiedIngredientSerializer
    queryset = QuantifiedIngredient.objects.all()


class IngredientView(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = '__all__'
    ordering = ['name']

    def get_serializer_class(self):
        if self.action == 'list':
            return IngredientNameSerializer
        else:
            return IngredientFullSerializer


class UnitView(viewsets.ModelViewSet):
    serializer_class = UnitSerializer
    queryset = Unit.objects.all()


class IngredientCategoryView(viewsets.ModelViewSet):
    serializer_class = IngredientCategorySerializer
    queryset = IngredientCategory.objects.all()


class LabelView(viewsets.ModelViewSet):
    serializer_class = LabelSerializer
    queryset = Label.objects.all()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = '__all__'
    ordering = ['name']