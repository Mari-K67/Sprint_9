from selenium.webdriver.common.by import By

class CreateRecipeLocators:
    CREATE_RECIPE_CHAPTER = (By.XPATH, "//a[@href='/recipes/create' and text()='Создать рецепт']")
    RECIPE_NAME = (By.XPATH, "//label[.//div[text()='Название рецепта']]//input")
    INGREDIENT = (By.XPATH, "//input[@type='text' and contains(@class, 'styles_ingredientsInput__1zzql')]")
    INGREDIENT_SAMPLE = (By.XPATH, "//div[contains(text(), 'абрикосовое варенье')]")
    INGREDIENT_WEIGHT = (By.XPATH, "//input[@type='text' and contains(@class, 'styles_ingredientsAmountValue__2matT')]")
    ADD_INGREDIENT = (By.XPATH, "//div[contains(text(), 'Добавить ингредиент')]")
    COOKING_TIME = (By.XPATH, "//label[.//div[text()='Время приготовления']]//input")
    DESCRIPTION = (By.XPATH, "//textarea[@rows='8' and contains(@class, 'styles_textareaField__1wfhC')]")
    DOWNLOAD_PHOTO = (By.XPATH, "//input[@class='styles_fileInput__3HjP3' and @type='file']")
    CREATE_RECIPE_BUTTON = (By.XPATH, "//button[text()='Создать рецепт']")

    RECIPE_TITLE = (By.XPATH, "//h1[contains(@class, 'styles_single-card__title')]")
    RECIPE_CHAPTER = (By.XPATH, "//a[@href='/recipes' and contains(text(), 'Рецепты')]")