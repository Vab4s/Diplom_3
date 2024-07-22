ORDERS_TEXT = ('xpath', '//h1[text()="Лента заказов"]')
ORDER_LINK = ('xpath', '//a[@class="OrderHistory_link__1iNby"]')
ORDER_CART = ('xpath', '//div[@class="Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X p-10"]')
ORDER_ID = ('xpath', '//p[text()="#098035"]')

ALL_TIME_COUNTER = ('xpath', '//p[text()="Выполнено за все время:"]//following-sibling::p[contains(@class, "OrderFeed_number")]')
TODAY_COUNTER = ('xpath', '//p[text()="Выполнено за сегодня:"]//following-sibling::p[contains(@class, "OrderFeed_number")]')