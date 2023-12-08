from . test_recipe_base import RecipeTestBase
from django.urls import reverse, resolve
from recipes import views
from unittest import skip

class RecipeCategoryViewTest(RecipeTestBase):


    def test_recipe_category_view_fuction_is_correct(self):
        view = resolve(reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertIs(view.func, views.category)

    def test_recipe_category_view_returns_404_if_no_recipes(self):
        response = self.client.get(reverse('recipes:category', kwargs={'category_id': 1000}))
        self.assertEqual(response.status_code, 404)

    def test_recipe_category_template_load_recipe(self):
        title = 'receita teste cetegory'
        self.make_recipe(title=title)
        response = self.client.get(reverse('recipes:category', kwargs={'category_id': 1}))
        content = response.content.decode('utf-8')
        self.assertIn(title, content)
        self.assertIn('1 pessoa', content)
        self.assertIn('5 minutos', content)

    def test_recipe_category_template_dont_load_recipes_not_published(self):
        recipe = self.make_recipe(is_published=False)
        response = self.client.get(reverse('recipes:recipe', kwargs={'id': recipe.category.id}))
        self.assertEqual(response.status_code, 404)