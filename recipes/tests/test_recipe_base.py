from django.test import TestCase
from recipes.models import Category, Recipe, User


class RecipeTestBase(TestCase):
    def setUp(self) -> None:
        return super().setUp()
    
    def make_category(self, name='carne de porco'):
        return Category.objects.create(name=name)
    
    def make_author(
        self,
        first_name = 'logi',
        last_name = 'tech',
        username = 'logi123',
        password = '123',
        email = 'logi@email.com',
    ):
        return User.objects.create_user(
            first_name = first_name,
            last_name = last_name,
            username = username,
            password = password,
            email = email,
        )
    
    def make_recipe(
        self,
        category_data = None,
        author_data = None,
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
    ):
        
        if category_data is None:
            category_data = {}

        if author_data is None:
            author_data = {}


        return Recipe.objects.create(
            category = self.make_category(**category_data),
            author = self.make_author(**author_data),
            title = title,
            description = description,
            slug = slug,
            preparation_time = preparation_time,
            preparation_time_unit = preparation_time_unit,
            servings = servings,
            servings_unit = servings_unit,
            preparation_steps = preparation_steps,
            preparation_steps_is_html = preparation_steps_is_html,
            is_published = is_published,
            cover = cover,
        )