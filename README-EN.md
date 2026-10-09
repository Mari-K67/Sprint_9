# Sprint_9
writing tests, building a Docker image, running the project in DockerCompose with Selenoid, setting up a pipeline for building the project in CI/CD.

Task: write auto-tests for the service ["Продуктовый помощник"](https://foodgram-frontend-1.foodgram.education-services.ru/signin) and set up CI/CD integration for them using GitHub as an example.  
Imagine that a manual tester handed you scenarios. They need to be covered with auto-tests.

## 1. Preparation
* Chrome browser is installed
* Selenium and Allure are connected.

## 2. Study of test scenarios
### Account creation
* Click the «Создать аккаунт» button.
* Fill in all the fields of the registration form and click the «Создать аккаунт» button.

**Check:**  
* Did the transition to the authorization page occur,
* is the authorization form displayed.

### Authorization
* Click the «Войти» button.
* Fill in all the fields of the authorization form and click the «Войти» button.

**Check:**  
* Did the transition to the home page occur,
* is the «Выход» button displayed.

### Recipe creation
* Authorize and go to the «Создать рецепт» tab.
* Fill in all the fields of the recipe creation form and click the «Создать рецепт» button.

Note (the ingredient must be added from the list, to display the list you need to start typing the ingredient name in the input field)

**Check if the following is displayed:**  
* card of the created recipe,
* the name that was filled in during creation.

## 3. Writing tests
1. Structure Page Object
- Describe the necessary locators using Page Object.
- Create a separate package for Page Object. 
- Create a separate class for each page with Page Object. 
2. Implement tests on Selenium
- Write tests on Selenium. Divide the tests by topic or functionality. 
Note: you do not need to create a separate class for each test. 
- Add tests for one functionality in one class. 
- All tests should be in the test directory. 
- Check that the tests run.

## 4. Creating a report in Allure
Generate an Allure report and push it to the repository.

## 5. Preparation of additional files for the sprint:
- `Dockerfile` for building the project image with tests,
- `docker-compose.yml` for building the project with selenoid,
- `ci.yml` for building the project with CI/CD based on GitHub Actions,
- screenshot of a successfully passed pipeline.
