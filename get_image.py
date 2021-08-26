# import requests
# from bs4 import BeautifulSoup as bs
#
# headers = {'accept': '*/*',
#            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0'}
# session = requests.Session()
# url = 'https://pixabay.com/ru/'
# temp = []
#
# html = """
# <div class="rc" data-hveid="53">
# <h3 class="r">
# <a href="https://billing.anapp.com/" onmousedown="return rwt(this,'','','','2','AFQjCNGqpb38ftdxRdYvKwOsUv5EOJAlpQ','m3fly0i1VLOK9NJkV55hAQ','0CDYQFjAB','','',event)">Billing: Portal Home</a>
# </h3>
# """
#
# def get_image():
#     request = session.get(url, headers=headers)
#     if request.status_code == 200:
#         soup_tmp = bs(html)
#
#         bs = BeautifulSoup(html)
#         elms = bs.select("h3.r a")
#         for i in elms:
#             print(i.attrs["href"])
#
# from bs4 import BeautifulSoup
#
# html = """
# <div class="rc" data-hveid="53">
# <h3 class="r">
# <a href="https://billing.anapp.com/" onmousedown="return rwt(this,'','','','2','AFQjCNGqpb38ftdxRdYvKwOsUv5EOJAlpQ','m3fly0i1VLOK9NJkV55hAQ','0CDYQFjAB','','',event)">Billing: Portal Home</a>
# </h3>
# """
#
# bs = BeautifulSoup(html)
# elms = bs.select("h3.r a")
# for i in elms:
#     print(i.attrs["href"])