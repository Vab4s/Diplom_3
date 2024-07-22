## Дипломный проект. Задание 3: Юнит-тесты

### Автотесты для проверки веб-приложения Stellar Burgers

### Структура проекта

Директория data:
    
    endpoints.py - API эндпоинты
    ingredients.py - список ингредиентов
    urls.py - необходимые ссылки

Директория helpers:

    create_order.py - создание заказа через АПИ запрос
    create_user.py - создание нового пользователя
    delete_user.py - удаление пользователя
    random_ingredient.py - генерация рандомного ингредиента, извлечение счётчика ингрелиента

Директория locators:
    
    general_locators.py - общие локаторы
    login_page_locators.py - локаторы страницы входа в аккаунт
    main_page_locators.py - локаторы главной страницы
    nav_menu_locators.py - локаторы меню сайта
    orders_page_locators.py - локаторы страницы ленты заказов
    profile_page_locators.py - локаторы страницы профиля
    reset_page_locators.py - локаторы страницы сброса пароля
    restore_password_page_locators.py - локаторы страницы аосстановления пароля

Директория pages:

    base_page.py - базовые методы
    login_page.py - методы страницы логина
    main_page.py - методы главной страницы
    order_history_page.py - методы траницы истории заказов
    orders_page.py - методы страницы ленты заказов
    profile_page.py - методы странцы профиля
    reset_password_page.py  - методы страницы сброса пароля
    restore_pass_page.py - методы страницы восстановления пароля

Директория tests:

    test_account.py - Проверка восстановления пароля
    test_main_functionality.py - Проверка личного кабинета
    test_orders_feed.py - Проверка основного функционала
    test_restore_password.py - Проверка раздела «Лента заказов»