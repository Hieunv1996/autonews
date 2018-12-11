import requests
from bs4 import BeautifulSoup
from news import News
import traceback


class VNExpress:
    def __init__(self, url):
        self.__url = url
        self.__news = None
        self.status = True

    def get(self):
        try:
            res = requests.get(self.__url)
            page_source = BeautifulSoup(res.text, 'lxml')
            title = page_source.select_one('h1.title_news_detail').get_text().strip()
            description = page_source.select_one('h2.description').get_text().strip()
            body = str(page_source.select_one('article.content_detail'))

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

    def is_valid(self):
        return self.__news is not None

    def get_news(self):
        return self.__news


if __name__ == '__main__':
    vne = VNExpress(
        'https://vnexpress.net/tin-tuc/the-gioi/trung-quoc-trieu-dai-su-my-yeu-cau-rut-lai-lenh-bat-giam-doc-huawei-3851592.html')
    vne.get()
    print(str(vne.get_news()))
