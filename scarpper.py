import requests
from bs4 import BeautifulSoup as Bs
class terraScrape:
    def image_scrape():
        re = requests.get('https://terraria.wiki.gg/wiki/Weapons') # defualt is weapons but there is also tools if you want them rember to remove some the last parts that it scrapes there are items
        soup = Bs(re.content, 'html.parser')

        temp = soup.find_all('span', attrs={'class' : 'i'})

        # print(temp[0].find('a')['href'].replace('/wiki/','') + '\n')
        items = []

        for item in range(len(temp) - 1):
            items.append(temp[item].find('a')['href'].replace('/wiki/', '') + '\n')
        print(items)

        f = open('tools.txt', 'w')

        f.writelines(items)
    # (temp[0].find('a')['href']).replace('/wiki/Weapons', '')
    def stats_scrape(item):
        re = requests.get('https://terraria.wiki.gg/wiki/' + item)
        soup = Bs(re.content, 'html.parser')
        
        temp = Bs(soup.find('table', attrs={'class' :'stat'}), 'html.parser')
    
        
        
terraScrape.stats_scrape('Terra_Blade')
    