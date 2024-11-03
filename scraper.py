import requests
from bs4 import BeautifulSoup as Bs

def find_anyIndex(lst, target, ind):
    indices = [i for i, value in enumerate(lst) if value == target]
    return indices[ind -1] if len(indices) > 1 else None

def extract_number(string):
    num_str = ''
    dot_found = False

    for char in string:
        if char.isdigit():
            num_str += char
        elif char == '.' and not dot_found:
            num_str += char
            dot_found = True
        else:
            if num_str:
                break

    return float(num_str) if num_str else None

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
        """"
        Type:
        Dmg:
        KB:
        Cc:
        Ut:
        Velo:
        Sell:
        """
        re = requests.get('https://terraria.wiki.gg/wiki/' + item)
        soup = Bs(re.content, 'html.parser')
        page_data = soup.find('table', attrs={'class' :'stat'})
        stats_data = page_data.find_all('tr')       
        
        # for i in stats:
        #     for j in stats_data:
        #         if 'Type' in i:
        if 'tooltip'in (stats_data[5].text).lower():
            stats_data.pop(5)

        if 'Ammo' in str(stats_data[1]):
            stats_data.pop(1)

        if 'Old-gen' in stats_data[1].text:
            sta = ''
            sta += str(extract_number(stats_data[1].text))
            sta += stats_data[1].text[find_anyIndex(stats_data[1].text, ')', 2) + 1:] #find_anyIndex(stats_data[1].text,')',2)
            stats_data[1] = sta
        else:
            stats_data[1] = stats_data[1].text

        if 'consumable' in stats_data[3].text.lower() or 'placeable' in stats_data[3].text.lower():
            stats_data.pop(3)
        #TODO make it so that all of the things have a n\a if the stats does not exist add back removed items
        stats = {'Type'      : str(stats_data[1][stats_data[1].index('(') + 1 : stats_data[1].index(')') ] ),
                 'Damage'    : int(extract_number(stats_data[1])), 
                 'KnockBack' : float(extract_number(stats_data[2].text)),
                 'CritChance': int(extract_number(stats_data[3].text)),
                 'UseTime'   : int(extract_number(stats_data[4].text))
                 }
        try:
            stats['Sell'] = stats_data[7].text[4:] 
        except:
            stats['Sell'] = 'n\\a'
        return stats 
