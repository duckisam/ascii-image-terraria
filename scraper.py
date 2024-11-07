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

def extract_attr(find_list, attrs_list): # finds a string with in a list of other string returns the first index of occuring or -1 if it is not in the list 
    temp = ['' for i in range(len(attrs_list))]
    for i in range(len(attrs_list) - 1):
        for j in range(len(find_list) - 1):
            if find_list[j] in attrs_list[j]:
                temp[i] = attrs_list[j] 
    return temp 

    

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
        stats_types = ['Type','Damage', 'KnockBack', 'Critical chance', 'Velocity', 'Tooltip', 'Rarity', 'Sell']
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
        stats_text = []
        for i in stats_data:
            stats_text.append(str(i.text))
        # for i in stats:
        #     for j in stats_data:
        #         if 'Type' in i:
        
        #TODO make it so that all of the things have a n\a if the stats does not exist add back removed items
        print(extract_attr(stats_text, stats_types))
        #print(extract_attr(['']))
       #try:
        #   stats['Sell'] = stats_data[7].text[4:] 
        #except:
        #    stats['Sell'] = 'n\\a'
        #return stats 
terraScrape.stats_scrape('Chain_Gun')
