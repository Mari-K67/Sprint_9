import allure
from pages.login_page import LoginPage
from locators.login_locators import LoginLocators
from data import Url
#python -B -m pytest tests/test_login.py

class TestCreateAccount:
    @allure.title('Вход в аккаунт')
    def test_login(self, driver):
        page = LoginPage(driver)

        page.login()

        assert page.get_current_url() == Url.RECIPES_PAGE_URL
        assert page.is_displayed(LoginLocators.LOGOUT_BUTTON)

