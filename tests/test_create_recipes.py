import allure
from pages.create_recipes_page import CreateRecipesPage
from locators.create_recipes_locators import CreateRecipeLocators
from data import RecipeData
#python -B -m pytest tests/test_create_recipes.py

class TestCreateRecipe:
    @allure.title('Создание рецепта')
    def test_create_recipe(self, driver):
        page = CreateRecipesPage(driver)

        page.login()
        page.create_recipes()

        assert page.is_displayed(CreateRecipeLocators.RECIPE_TITLE)
        assert page.get_text(CreateRecipeLocators.RECIPE_TITLE) == RecipeData.RECIPE_NAME