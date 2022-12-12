# BTC_bot выводит информацию о последней цене на BTC 
 * import requests, telebot,datetime
 * C помощью библиотеки requests отправляеться GET запрос на сайт с API
 * функция start_message обернутая в декоратор @bot.message.handler выводит приветсвие
 * в декораторе @bot.message.handler(content_types=["text"]). С помощью requests отправляеться GET запрос на сайт с API и методом json сохраняем в переменную sell_price, функция get_text реагирует на полученное сообщение и если строка равна price то определяет стоимость битка на текущую дату 