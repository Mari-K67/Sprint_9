from faker import Faker

fake = Faker()

class Url:
    MAIN_URL = 'https://foodgram-frontend-1.foodgram.education-services.ru'
    SIGNUP_URL = f'{MAIN_URL}/signup'
    RECIPES_PAGE_URL = f'{MAIN_URL}/recipes'
    
class UserBody:
    def __init__(self):
        self.name = fake.first_name()
        self.surname = fake.last_name()
        self.user_name = fake.user_name()
        self.email = f"{self.user_name}@mail.ru"
        self.password = fake.password(length=12, special_chars=False)

    fix_email = 'www111@mai.ru'
    fix_password = '12345fdfdf'

class RecipeData: 
    RECIPE_NAME = 'тест'
    INGREDIENT = 'абрикосовое варенье'
    INGREDIENT_WEIGHT = 15 
    COOKING_TIME = 15
    DESCRIPTION = 'что-то'
    PHOTO_LINK = 'C:/Users/M.Komarova/Desktop/ALL/IMAGE-TO-VIDEO/Animal_Category/bird.jpg'