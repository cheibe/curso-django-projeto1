from . test_recipe_base import RecipeTestBase
from django.urls import reverse, resolve
from recipes import views
from unittest import skip

class RecipeDetailViewTest(RecipeTestBase):

    def test_recipe_detail_view_fuction_is_correct(self):
        view = resolve(reverse('recipes:recipe', kwargs={'id': 2}))
        self.assertIs(view.func, views.recipe)

    def test_recipe_detail_view_returns_404_if_no_recipes(self):
        response = self.client.get(reverse('recipes:recipe', kwargs={'id': 500}))
        self.assertEqual(response.status_code, 404)

    def test_recipe_detail_template_load_the_correct_recipe(self):
        title = 'receita teste detail'
        self.make_recipe(title=title)
        response = self.client.get(reverse('recipes:recipe', kwargs={'id': 1}))
        content = response.content.decode('utf-8')
        self.assertIn(title, content)
        self.assertIn('1 pessoa', content)
        self.assertIn('5 minutos', content)

    def test_recipe_detail_template_dont_load_recipe_not_published(self):
        recipe = self.make_recipe(is_published=False)
        response = self.client.get(reverse('recipes:recipe', kwargs={'id': recipe.id}))
        self.assertEqual(response.status_code, 404)