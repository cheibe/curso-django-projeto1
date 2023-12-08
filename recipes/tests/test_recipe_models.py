from .test_recipe_base import RecipeTestBase, Recipe
from django.core.exceptions import ValidationError
from parameterized import parameterized

class RecipeModelTest(RecipeTestBase):
    def setUp(self) -> None:
        self.recipe = self.make_recipe()
        return super().setUp()

    def make_recipe_no_default(self):
        recipe = Recipe(
            category = self.make_category(name='test default category'),
            author = self.make_author(username='username'),
            title = 'receita teste',
            description = 'receita teste descrição',
            slug = 'receita-teste-slug-for-no-defaults',
            preparation_time = 5,
            preparation_time_unit = 'minutos',
            servings = 1,
            servings_unit = 'pessoa',
            preparation_steps = 'etapas da receita teste',
        )
        recipe.full_clean()
        recipe.save()
        return recipe
    
    @parameterized.expand([
            ('title', 65),
            ('description', 165),
            ('preparation_time_unit', 65),
            ('servings_unit', 65),
        ])
    def test_recipe_fields_max_length(self, field, max_length):
        setattr(self.recipe, field, 'A' * (max_length + 1))
        with self.assertRaises(ValidationError):
            self.recipe.full_clean()

    def test_recipe_preparation_steps_is_html_is_false_by_default(self):
        recipe = self.make_recipe_no_default()
        self.assertFalse(recipe.preparation_steps_is_html)

    def test_recipe_is_published_is_false_by_default(self):
        recipe = self.make_recipe_no_default()
        self.assertFalse(recipe.is_published)

    def test_recipe_string_representations(self):
        self.recipe.title = 'testing representation'
        self.recipe.full_clean()
        self.recipe.save()
        self.assertEqual(str(self.recipe), 'testing representation')