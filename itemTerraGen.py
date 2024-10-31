from bs4 import BeautifulSoup as Bs
import requests
from PIL import Image
from ascii_magic import AsciiArt as Aa # i hate this thing i made my own
import io
import random as r
import asciiCon as Ac
from scarpper import terraScrape


items_txt = open('item.txt', 'r')

items_ls = items_txt.readlines()
items = []
for item in items_ls:
    items.append(item.replace('\n',''))



rand_item = items[r.randint(0, len(items))]

while True:
    try:
        re = requests.get('https://terraria.wiki.gg/wiki/'+ rand_item )  
        break
    except:
        continue


soup = Bs(re.content, 'html.parser')
images = soup.find_all('img')
sprite_link = ''
for i in range(len(images)):
    if rand_item.lower() in str(images[i].get('src')).lower():
        print(i, ' is the index and ', images[i].get('src'), 'is the link')
        sprite_link = images[i].get('src')
        break


sprite_data = requests.get('https://terraria.wiki.gg' + sprite_link).content

Ac.Ascii_Png_converter.create_ascii_from_bytes(sprite_data, True, 2)

# print(terraScrape.stats_scrape(rand_item))