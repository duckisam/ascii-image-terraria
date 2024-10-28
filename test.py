import requests
from bs4 import BeautifulSoup as Bs
re = requests.get('https://terraria.wiki.gg/wiki/Tools')
soup = Bs(re.content, 'html.parser')

temp = soup.find_all('span', attrs={'class' : 'i'})

# print(temp[0].find('a')['href'].replace('/wiki/','') + '\n')
items = []

for item in range(len(temp) - 1):
    items.append(temp[item].find('a')['href'].replace('/wiki/', '') + '\n')
print(items)

f = open('tools.txt', 'w')

f.writelines(items, monochrome=True)
# (temp[0].find('a')['href']).replace('/wiki/Weapons', '')

    