from . test_recipe_base import RecipeTestBase
from django.urls import reverse, resolve
from recipes import views
from unittest import skip

class RecipeViewsTest(RecipeTestBase):

    def test_recipe_home_view_fuction_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)

    def test_recipe_home_view_returns_status_code_200_OK(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_view_loads_correct_template(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    def test_recipe_home_template_shows_no_recipes_found_if_no_recipes(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertIn('<h1>NO RECIPES FOUND HERE 😢</h1>', response.content.decode('utf-8'))

    def test_recipe_home_template_load_recipe(self):
        self.make_recipe()
        response = self.client.get(reverse('recipes:home'))
        content = response.content.decode('utf-8')
        response_context_recipes = response.context['recipes']
        self.assertIn('receita teste', content)
        self.assertIn('1 pessoa', content)
        self.assertIn('5 minutos', content)
        self.assertEqual(len(response_context_recipes), 1)


    def test_recipe_category_view_fuction_is_correct(self):
        view = resolve(reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertIs(view.func, views.category)

    def test_recipe_category_view_returns_404_if_no_recipes(self):
        response = self.client.get(reverse('recipes:category', kwargs={'category_id': 1000}))
        self.assertEqual(response.status_code, 404)

    def test_recipe_detail_view_fuction_is_correct(self):
        view = resolve(reverse('recipes:recipe', kwargs={'id': 2}))
        self.assertIs(view.func, views.recipe)

    def test_recipe_detail_view_returns_404_if_no_recipes(self):
        response = self.client.get(reverse('recipes:recipe', kwargs={'id': 500}))
        self.assertEqual(response.status_code, 404)

    