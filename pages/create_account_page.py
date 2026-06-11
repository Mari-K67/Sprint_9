import allure
from .base_page import BasePage
from locators.create_account_locators import CreateAccountLocators
from data import UserBody

class CreateAccountPage(BasePage):
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
