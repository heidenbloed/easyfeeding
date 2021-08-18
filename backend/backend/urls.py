"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import urls as auth_urls
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from recipe_db import views


router = routers.DefaultRouter()
router.register(r'recipes', views.RecipeView, 'recipe')
router.register(r'ingredients', views.IngredientView, 'ingredient')
router.register(r'quantified_ingredients', views.QuantifiedIngredientView, 'quantified_ingredient')
router.register(r'recipe_image', views.RecipeImageView, 'recipe_image')
router.register(r'units', views.UnitView, 'unit')
router.register(r'ingredient_categories', views.IngredientCategoryView, 'ingredient_category')
router.register(r'labels', views.LabelView, 'label')


schema_view = get_schema_view(
   openapi.Info(
      title="Recipe DB API",
      default_version='v1'
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('accounts/', include(auth_urls)),
    re_path(r'^swagger(?P<format>.json|.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
