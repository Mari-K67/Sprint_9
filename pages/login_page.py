import allure
from .base_page import BasePage
from locators.create_account_locators import CreateAccountLocators
from locators.login_locators import LoginLocators
from data import UserBody

class LoginPage(BasePage):
    def create_account(self):

        user = UserBody()

        with allure.step('1. кликнуть на кнопку "Создать аккаунт"'):
            self.click(CreateAccountLocators.CREATE_ACCOUNT_CHAPTER)

        with allure.step('2. заполнить информацию o пользователе'):
            self.send_keys(CreateAccountLocators.NAME_FIELD, user.name)
            self.send_keys(CreateAccountLocators.SURNAME_FIELD, user.surname)
            self.send_keys(CreateAccountLocators.USER_NAME, user.user_name)
            self.send_keys(CreateAccountLocators.EMAIL_FIELD, user.email)
            self.send_keys(CreateAccountLocators.PASSWORD_FIELD, user.password)

        with allure.step('3. ликнуть на кнопку "Создать аккаунт"'):
            self.scroll_to_botton()
            self.click(CreateAccountLocators.CREATE_ACCOUNT_BUTTON)

        return user.user_name, user.password
    
    def login(self):
        with allure.step('1. Создать аккаунт'):
            user_name, password = self.create_account()

        with allure.step('2. ожидание перехода на страницу входа'):
            self.wait_element_visibility(LoginLocators.LOG_INTO_WEBSITE_TITLE)

        #Вход происходит не по email, а по  user_name
        #ОШИБКА 
        with allure.step('3. ввести email и пароль'):
            self.send_keys(LoginLocators.EMAIL_FIELD, user_name)
            self.send_keys(LoginLocators.PASSWORD_FIELD, password)

        with allure.step('4. нажать кнопку "Войти"'):
            self.click(LoginLocators.LOGIN_BUTTON)

        with allure.step('5. ожидание перехода на главную страницу'):
            self.wait_element_visibility(LoginLocators.RECIPES_TITLE)