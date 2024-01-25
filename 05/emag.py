from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import exceptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import pandas as pd

option = webdriver.FirefoxOptions()
option.add_argument('start-maximized')

driver = webdriver.Firefox(service = FirefoxService(GeckoDriverManager().install()), options = option)
driver.get('https://www.emag.ro/#opensearch')

searchBox = driver.find_element(by = By.ID, value = 'searchboxTrigger')
searchBox.send_keys("laptop")
searchBox.submit()

element = driver.find_elements(by = By.CLASS_NAME, value = 'card-item')

product_list, price_list, list_of_elements = [], [], []
# for i in element:
#     try:
#         product = i.find_element(by = By.CLASS_NAME, value = 'card-v2-title')
#         product_list.append(product.text)
#         price = i.find_element(by = By.CLASS_NAME, value = 'product-new-price')
#         price_list.append(price.text)
#     except exceptions.NoSuchElementException:
#         pass
#
# print(product_list)
# print(price_list)
# list_of_elements.append(product_list)
# list_of_elements.append(price_list)
#
# df = pd.DataFrame(list_of_elements).transpose()
# df.to_csv("elemente.csv")

dictionary = {f"Laptop {i}": [] for i in range(1, len(element) + 1)}
for i, v in enumerate(element):
    try:
        product = v.find_element(by = By.CLASS_NAME, value = 'card-v2-title')
        product_list.append(product.text)
        price = v.find_element(by = By.CLASS_NAME, value = 'product-new-price')
        price_list.append(price.text)

        dictionary[f"Laptop {i}"].append(product.text, price.text)
    except exceptions.NoSuchElementException:
        pass

print(dictionary)