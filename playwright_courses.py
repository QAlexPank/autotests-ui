from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Открыть страницу регистрации
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    # Заполнить форму регистрации и нажать на кнопку "Registration"
    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill('user.name@gmail.com')

    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill('username')

    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill('password')

    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    # Сохранить состояние браузера
    context.storage_state(path="browser-state.json")

# Создать новую сессию браузера
with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="browser-state.json")
    page = context.new_page()

    # Открыть страницу "Courses"
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    # Проверить наличие и текст заголовка "Courses"
    courses_title = page.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_title).to_be_visible()
    expect(courses_title).to_have_text('Courses')

    # Проверить наличие и текст блока "There is no results"
    empty_view_icon = page.get_by_test_id('courses-list-empty-views-icon')
    expect(empty_view_icon).to_be_visible()

    # Проверить наличие и видимость иконки пустого блока
    empty_view_title = page.get_by_test_id('courses-list-empty-views-title-text')
    expect(empty_view_title).to_be_visible()
    expect(empty_view_title).to_have_text('There is no results')

    # Проверить наличие и текст описания блока: "Results from the load test pipeline will be displayed here"
    empty_view_description = page.get_by_test_id('courses-list-empty-views-description-text')
    expect(empty_view_description).to_be_visible()
    expect(empty_view_description).to_have_text('Results from the load test pipeline will be displayed here')
