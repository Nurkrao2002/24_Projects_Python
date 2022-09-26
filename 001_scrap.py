import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://en.wikipedia.org/wiki/Josh_(2000_film)")
soup = BeautifulSoup(html, "html.parser")
table = soup.findAll("table", {"class":"wikitable"})[0]
rows = table.findAll("tr")

# with open("joshfilmy.csv", "wt+", newline="") as f:
#     writer = csv.writer(f)
#     for i in rows:
#         row = []
#         for cell in i.findAll(["td", "th"]):
#             row.append(cell.get_text())
#         writer.writerow(row)
   
import pandas as pd
a = pd.read_csv("joshfilmy.csv")
print(a)
print(a.shape)