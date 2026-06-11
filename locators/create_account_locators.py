from selenium.webdriver.common.by import By

class CreateAccountLocators:
    CREATE_ACCOUNT_CHAPTER = (By.XPATH, "//a[@href='/signup' and normalize-space()='Создать аккаунт']")
    NAME_FIELD = (By.XPATH, "//input[@name='first_name']")
    SURNAME_FIELD = (By.XPATH, "//input[@name='last_name']")
    USER_NAME = (By.XPATH, "//input[@name='username']")
    EMAIL_FIELD = (By.XPATH, "//input[@name='email']")
    PASSWORD_FIELD = (By.XPATH, "//input[@name='password']")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Создать аккаунт']")