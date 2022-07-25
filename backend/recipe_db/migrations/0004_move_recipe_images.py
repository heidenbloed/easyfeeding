# Generated by Django 3.2.14 on 2022-07-24 20:46
import os

from django.db import migrations
from django.conf import settings
from django.utils.crypto import get_random_string


def move_recipe_images(apps, schema_editor):
    RecipeImageModel = apps.get_model('recipe_db', 'RecipeImage')
    for recipe_image in RecipeImageModel.objects.all():
        if not recipe_image.image.name.startswith("recipe_images"):
            old_path = recipe_image.image.path
            if os.path.exists(old_path):
                new_name = os.path.join("recipe_images",  recipe_image.image.name)
                new_path = os.path.join(settings.MEDIA_ROOT, new_name)
                while os.path.exists(new_path):
                    new_name, ext = os.path.splitext(new_name)
                    new_name = f"{new_name}_{get_random_string(7)}{ext}"
                    new_path = os.path.join(settings.MEDIA_ROOT, new_name)
                os.rename(old_path, new_path)
                recipe_image.image.name = new_name
                recipe_image.save()


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_db', '0003_alter_recipeimage_image'),
    ]

    operations = [
        migrations.RunPython(move_recipe_images, reverse_code=migrations.RunPython.noop),
    ]
