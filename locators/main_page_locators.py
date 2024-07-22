SECTION_CREATE_BURGER = ('xpath', '//section[@class="BurgerIngredients_ingredients__1N8v2"]')
INGREDIENT = ('xpath', '//a[contains(@class, "BurgerIngredient")]')

INGREDIENT_BUN_PURPLE = ('xpath', '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa6d"]')
INGREDIENT_BUN_CYAN = ('xpath', '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa6c"]')
INGREDIENT_BUN_PURPLE_COUNTER = ('xpath', '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa6d"]//p[contains(@class, "counter_counter__num")]')
INGREDIENT_BUN_CYAN_COUNTER = ('xpath', '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa6c"]//p[contains(@class, "counter_counter__num")]')

MODAL_SECTION_INGREDIENT = ('xpath', '//h2[text()="Детали ингредиента"]/ancestor::section[contains(@class, "Modal_modal__P3_V5")]')
MODAL_SECTION_ORDER = ('xpath', '//p[text()="идентификатор заказа"]//ancestor::section[contains(@class, "Modal_modal__P3_V5")]')
BUTTON_MODAL_CLOSE = ('xpath', '(//button[contains(@class, "Modal_modal__close__TnseK")])[1]')
BASKET_SECTION = ('xpath', '//section[@class="BurgerConstructor_basket__29Cd7 mt-25 "]')
CONSTRUCTOR_AREA = ('xpath', '//*[contains(@class, "BurgerConstructor_basket")]')

BUTTON_MAKE_ORDER = ('xpath', '//button[text()="Оформить заказ"]')