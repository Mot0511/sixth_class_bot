import requests
from bs4 import BeautifulSoup as bs

headers = {'accept': '*/*',
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0'}
session = requests.Session()
url = 'https://www.gismeteo.ru/weather-kirov-4292/'
temp = []

def get_weather():
    request = session.get(url, headers=headers)
    if request.status_code == 200:
        # start parsing
        soup_tmp = bs(request.content, 'lxml')

        temp.append(soup_tmp.find_all('span', attrs={'class': 'js_value tab-weather__value_l'}))

        return temp[0][0].text.replace(' ', '')