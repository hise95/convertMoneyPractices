import requests
from lxml import html

date_input = input("Please enter the date: ")
r = requests.get(f"https://bank.gov.ua/ua/markets/exchangerates?date={date_input}&period=daily")
tree = html.fromstring(r.content)
shortened = '//*[@id="exchangeRates"]/tbody/tr[.//td[contains(text(), "EUR")]]/td[last()]/text()'
print(tree.xpath(shortened))