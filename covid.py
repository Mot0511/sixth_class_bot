import requests
from bs4 import BeautifulSoup as bs

headers = {'accept': '*/*',
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0'}
session = requests.Session()
rus_url = 'https://xn--80aesfpebagmfblc0a.xn--p1ai/information/'
rus_kirov = 'https://xn--80aesfpebagmfblc0a.xn--p1ai/information/'


rus = []

kirov_new = []
kirov_well = []
kirov_kills = []

def get_covid():
    request = session.get(rus_url, headers=headers)
    if request.status_code == 200:
        # start parsing
        soup_tmp = bs(request.content, 'lxml')

        rus.append(soup_tmp.find_all('h3', attrs={'class': 'cv-stats-virus__item-value'}))

        print(rus)