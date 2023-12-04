from django.test import TestCase
from recipes.models import Category, Recipe, User


class RecipeTestBase(TestCase):
    def setUp(self) -> None:
        category = Category.objects.create(name='carne de porco')
        author = User.objects.create_user(
            first_name = 'logi',
            last_name = 'tech',
            username = 'logi123',
            password = '123',
            email = 'logi@email.com',
        )
        recipe = Recipe.objects.create(
            category = category,
            author = author,
            title = 'receita teste',
            description = 'receita teste descrição',
            slug = 'receita-teste-slug',
            preparation_time = 5,
            preparation_time_unit = 'minutos',
            servings = 1,
            servings_unit = 'pessoa',
            preparation_steps = 'etapas da receita teste',
            preparation_steps_is_html = False,
            is_published = True,
            cover = False,
        )
        return super().setUp()