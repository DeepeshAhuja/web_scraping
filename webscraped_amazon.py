import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = "https://www.amazon.in/s?k=laptop&page={}"

titles = []
prices = []
no_of_pages = 15

for page in range(1,no_of_pages+1 ):
    url = base_url.format(page)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    for product in soup.find_all('div', {'data-component-type': 's-search-result'}):
        title = product.find('h2').find('span').text.strip()
        price = product.find('span', {'class': 'a-price-whole'}).text.strip()
        titles.append(title)
        prices.append(price)

df = pd.DataFrame({'Title': titles, 'Price': prices})
print(df)

