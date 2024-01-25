from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import pandas as pd

option = webdriver.FirefoxOptions()
option.add_argument('start-maximized')

driver = webdriver.Firefox(service = FirefoxService(GeckoDriverManager().install()), options = option)
driver.get("https://www.bnr.ro/files/xml/nbrfxrates2022.htm")

table = driver.find_element(by = By.XPATH, value = '//*[@id="Data_table"]')

lista = table.text.split('\n')

header = driver.find_element(by = By.XPATH, value = '//*[@id="Data_table"]/table/thead/tr').text.split('\n')

dictionary = {i: [] for i in header}
print(dictionary)

for i in range(0, len(header)):
    for j in range(len(header) + int(i), len(lista), len(header)):
        dictionary[header[int(i)]].append(lista[j])

print(dictionary)

df = pd.DataFrame(dictionary)
df.to_csv("all_data.csv")