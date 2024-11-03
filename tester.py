from bs4 import BeautifulSoup as Bs
import requests
from PIL import Image
import random as r
import asciiCon as Ac
from scraper import terraScrape
import itemTerraGen as Tgen

def find_anyIndex(lst, target, ind):
    indices = [i for i, value in enumerate(lst) if value == target]
    return indices[ind -1] if len(indices) > 1 else None
count = 0
items_txt = open('item.txt', 'r')

items_ls = items_txt.readlines()
items = []
for item in items_ls:
    items.append(item.replace('\n',''))
for i in range(len(items)):
    item = items[i]
    print(Tgen.itemGen(item))
    print(terraScrape.stats_scrape(item))    
    print(item, ' is the item and the line number ', i + 1)

# print(terraScrape.stats_scrape(rand_item))
