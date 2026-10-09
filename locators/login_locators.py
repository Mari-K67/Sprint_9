from selenium.webdriver.common.by import By

class LoginLocators:
    EMAIL_FIELD = (By.XPATH, "//input[@name='email']")
    PASSWORD_FIELD = (By.XPATH, "//input[@name='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    LOGIN_CHAPTER = (By.XPATH, "//a[@href='/signin' and normalize-space(.)='Войти']")
    LOG_INTO_WEBSITE_TITLE = (By.XPATH, "//h1[text()='Войти на сайт']")
    LOGOUT_BUTTON = (By.XPATH, "//a[text()='Выход']")
    RECIPES_TITLE = (By.XPATH, "//h1[text()='Рецепты']")
