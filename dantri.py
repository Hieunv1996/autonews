import requests
from bs4 import BeautifulSoup
from news import News
import traceback


class Dantri:
    def __init__(self, url):
        self.__url = url
        self.__news = None
        self.status = True

    def get(self):
        try:
            res = requests.get(self.__url)
            page_source = BeautifulSoup(res.text, 'lxml')
            title = page_source.select_one('div#ctl00_IDContent_ctl00_divContent > h1.fon31.mgb15').get_text().strip()
            description = page_source.select_one('h2.fon33.mt1.sapo').get_text().strip()
            body = str(page_source.select_one('div#divNewsContent'))

            if title and description and body:
                self.__news = News(self.__url, title, description, body)
        except:
            self.status = False
        return None

    def is_valid(self):
        return self.__news is not None

    def get_news(self):
        return self.__news

    def print_log(self):
        if self.status:
            print('SUCCESS: ' + self.__url)
        else:
            print('FAILED:  ' + self.__url)


if __name__ == '__main__':
    vne = Dantri(
        'https://dantri.com.vn/xa-hoi/chu-tich-ha-noi-lan-dau-cong-bo-so-tien-chi-de-trong-1-trieu-cay-xanh-20181210113402318.htm')
    vne.get()
    print(str(vne.get_news()))
