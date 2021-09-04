from requests_html import *

def get_covid():
    sess = HTMLSession()
    r = sess.get('https://xn--80aesfpebagmfblc0a.xn--p1ai/information/')
    rus_new = r.html.find('.cv-stats-virus__item-value')
    print(rus_new)