import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the URLs to scrape
urls = ['https://www.billtrack50.com/legislatordetail/2226', 'https://www.billtrack50.com/legislatordetail/1613', 'https://www.billtrack50.com/legislatordetail/24709']

# Define the data to be scraped

res = []
# Loop through the URLs
for url in urls:
    # Send a GET request to the website
    response = requests.get(url)

    # Parse the HTML content using Beautiful Soup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract the data
    if 'https://www.billtrack50.com/legislatordetail/2226' in url:
        # Scrape for Senator Liz Krueger


        krueger = soup.find('div',class_='layout-content').find('main').find('div').find('div').find('div',class_='tab-content').find(class_='tab-pane fade show active').find('table').findAll('tr')#[1].findAll('td')
        for i in krueger[1:100]:
            data = {}
            data['Politician'] = 'Liz Krueger'
            data['Bill'] = i.findAll('td')[0].get_text()[1:-1]
            data['Bill_Name'] = i.findAll('td')[1].get_text()
            data['Summary'] = i.findAll('td')[2].get_text()
            data['Progress'] = i.findAll('td')[3].get_text()
            res.append(data)

    elif 'https://www.billtrack50.com/legislatordetail/24709' in url:
        # Scrape for Representative Jason Stephens
        jason = soup.find('div', class_='layout-content').find('main').find('div').find('div').find('div',
                                                                                                      class_='tab-content').find(
            class_='tab-pane fade show active').find('table').findAll('tr')  # [1].findAll('td')
        for i in jason[1:100]:
            data = {}
            data['Politician'] = 'Jason Stephens'
            data['Bill'] = i.findAll('td')[0].get_text()[1:-1]
            data['Bill_Name'] = i.findAll('td')[1].get_text()
            data['Summary'] = i.findAll('td')[2].get_text()
            data['Progress'] = i.findAll('td')[3].get_text()
            res.append(data)

    elif 'https://www.billtrack50.com/legislatordetail/1613' in url:
        # Scrape for Delegate Kathy J. Byron
        kathy = soup.find('div', class_='layout-content').find('main').find('div').find('div').find('div',
                                                                                                      class_='tab-content').find(
            class_='tab-pane fade show active').find('table').findAll('tr')  # [1].findAll('td')
        for i in kathy[1:100]:
            data = {}
            data['Politician'] = 'Kathy J. Byron'
            data['Bill'] = i.findAll('td')[0].get_text()[1:-1]
            data['Bill_Name'] = i.findAll('td')[1].get_text()
            data['Summary'] = i.findAll('td')[2].get_text()
            data['Progress'] = i.findAll('td')[3].get_text()
            res.append(data)

# Create a Pandas DataFrame from the data
df = pd.DataFrame(res)

# Write the data to a CSV file
df.to_csv('politician_environmental_policies.csv', index=False)
