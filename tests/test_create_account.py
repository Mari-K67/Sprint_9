import allure
from pages.create_account_page import CreateAccountPage
from locators.login_locators import LoginLocators
#python -B -m pytest tests/test_create_account.py

class TestCreateAccount:
    @allure.title('Создание аккаунта')
    def test_create_account(self, driver):
        page = CreateAccountPage(driver)
        page.create_account()

        assert page.is_displayed(LoginLocators.LOG_INTO_WEBSITE_TITLE)
        assert page.is_displayed(LoginLocators.EMAIL_FIELD)