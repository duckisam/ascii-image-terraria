import asciiCon as Ac
import itemTerraGen as terraGen
import scraper as terraScrape
import random 

itemsTxt = open('item.txt', 'r')
items = []
imgTxt = open('img.txt', 'w', encoding='utf-8')

for i in itemsTxt:
    items.append(i.replace('\n', ''))
random_item = str(items[random.randint(0, len(items) - 1)])
imgTxt.write(terraGen.itemGen(random_item))





