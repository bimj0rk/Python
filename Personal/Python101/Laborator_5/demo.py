import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

req = requests.get('https://en.wikipedia.org/wiki/https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States')
soup = bs(req.content, 'html.parser')
table = soup.table.tbody
rows = table.find_all('tr')
data = []
for row in rows:
    trs = row.find_all('td')
    if len(trs) > 0:
        x = []
        name_element = trs[1]
        x.append(name_element.b.a.text)
        
        party_element = trs[4]
        if party_element.i != None:
            x.append(party_element.i.string)
        else:
            x.append(party_element.a.text)
        data.append(x)
            
df = pd.DataFrame(data, columns=['Name', 'Party'])
df.to_csv('presidents.csv', index = False)