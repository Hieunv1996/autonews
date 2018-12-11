import requests
from bs4 import BeautifulSoup
from news import News
import traceback


class Tuoitre:
    def __init__(self, url):
        self.__url = url
        self.__news = None
        self.status = True

    def get(self):
        try:
            res = requests.get(self.__url)
            page_source = BeautifulSoup(res.text, 'lxml')
            title = page_source.select_one('h1.article-title').get_text().strip()
            description = page_source.select_one('h2.sapo').get_text().strip()
            body = str(page_source.select_one('div#main-detail-body'))

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
    vne = Tuoitre(
        'https://tuoitre.vn/hai-ba-chau-thoat-chet-gang-tac-khi-bi-xe-container-mat-lai-lao-vao-20181210142449073.htm')
    vne.get()
    print(str(vne.get_news()))
