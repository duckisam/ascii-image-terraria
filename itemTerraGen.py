from bs4 import BeautifulSoup as Bs
import requests
from PIL import Image
from ascii_magic import AsciiArt as Aa # i hate this thing i made my own
import io
import random as r
import asciiCon as Ac
#from scraper import terraScrape


def itemGen(itemTXT, toItem= False):

    re = requests.get('https://terraria.wiki.gg/wiki/'+ itemTXT )  
    soup = Bs(re.content, 'html.parser')
    images = soup.find_all('img')
    sprite_link = ''
    for i in range(len(images)):
        if itemTXT.lower() in str(images[i].get('src')).lower():
            print(i, ' is the index and ', images[i].get('src'), 'is the link')
            sprite_link = images[i].get('src')
            break
    
    
    sprite_data = requests.get('https://terraria.wiki.gg' + sprite_link).content

    return Ac.Ascii_Png_converter.create_ascii_from_bytes(sprite_data, False, 2)
    
# print(terraScrape.stats_scrape(rand_item))




