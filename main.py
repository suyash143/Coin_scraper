import requests
from bs4 import BeautifulSoup
import csv
res = requests.get('https://coinstats.app/coins/')
htmlcontent=res.content
soup = BeautifulSoup(htmlcontent,'html.parser')

products=soup.select('div.coin-with-logo>span')
prices=soup.find_all('span',class_='price other-color')
cap=soup.find_all('span',class_="cap other")
btc=soup.select('td.right>a>span.other-color')
vol=soup.select('td.right>a>span.cap')

with open('names.csv', 'w', newline='') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(["Name","Price","Market Cap","Price in BTC","Volume in 24 Hours"])
    for i in range(len(prices)):
        writer.writerow([f'{products[i].text.split()[0]}',f'{prices[i].text}',f'{cap[i].text}',
                         f'{btc[1::2][i].text}',f'{vol[i].text}'])