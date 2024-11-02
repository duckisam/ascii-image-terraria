from bs4 import BeautifulSoup as Bs
import requests
from PIL import Image
import io
import random as r
import asciiCon as Ac
#from scraper import terraScrape

def find_anyIndex(lst, target, ind):
    indices = [i for i, value in enumerate(lst) if value == target]
    return indices[ind -1] if len(indices) > 1 else None

count = 0
items_txt = open('item.txt', 'r')

items_ls = items_txt.readlines()
items = []
for item in items_ls:
    items.append(item.replace('\n',''))
for i in range(len(items) - 1):
    item = items[i]
    try:
        while True:
            try:
                re = requests.get('https://terraria.wiki.gg/wiki/'+ item )  
                break
            except:
                continue


        soup = Bs(re.content, 'html.parser')
        images = soup.find_all('img')
        sprite_link = ''
        for i in range(len(images)):
            if item.lower() in str(images[i].get('src')).lower():
                print(i, ' is the index and ', images[i].get('src'), 'is the link')
                sprite_link = images[i].get('src')
                break


        sprite_data = requests.get('https://terraria.wiki.gg' + sprite_link).content
        Ac.Ascii_Png_converter.create_ascii_from_bytes(sprite_data, True, 2)
        print(terraScrape.stats_scrape(item))
    except: 
        print(item, ' at line ', + count + 1, ' has and erorr')
    count +=1

    ir = input('Press any key to move on or -1 to quit')

    if ir == '-1':
        break
# print(terraScrape.stats_scrape(rand_item))
