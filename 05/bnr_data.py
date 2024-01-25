import requests as requests
from bs4 import BeautifulSoup
import pandas as pd

req = requests.get("https://www.bnr.ro/Cursul-de-schimb--7372.aspx")
link = BeautifulSoup(req.text, 'html.parser')
# print(link)

title = link.find_all("div", attrs = {"class": "contentDiv"})

dataSet = []

for row in title[0].find_all("table"):
    for data in row.find_all("tr"):
        if data.find_all("th"):
            header = []
            for th in data.find_all("th"):
                header.append(th.get_text())
            dataSet.append(header)
        dates = []
        for index, value in enumerate(data.find_all("td")):
            if index == 0:
                dates.append(value.get_text())
            else:
                dates.append(value.get_text().strip().replace(",", "."))
        dataSet.append(dates)

print(dataSet)

df = pd.DataFrame(dataSet)
print(df)
df.to_csv('date_bnr.csv')