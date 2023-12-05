from .test_recipe_base import RecipeTestBase, Recipe
from django.core.exceptions import ValidationError
from parameterized import parameterized

class RecipeCategoryModelTest(RecipeTestBase):
    def setUp(self) -> None:
        self.category = self.make_category(name='category testing')
        return super().setUp()

    def test_recipe_category_model_string_representarion_is_name_field(self):
        self.assertEqual(str(self.category), self.category.name)

    def test_recipe_category_model_name_max_length_is_65_chars(self):
        self.category.name = 'A' * 70
        with self.assertRaises(ValidationError):
            self.category.full_clean()
