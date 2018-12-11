import feedparser
import json
from news import News
import traceback
from tuoitre import Tuoitre
from dantri import Dantri
from vnexpress import VNExpress


def call_crawler(url, log):
    news = None
    if 'tuoitre.vn' in url:
        tto = Tuoitre(url)
        tto.get()
        if log:
            tto.print_log()
        if tto.is_valid():
            news = tto.get_news()
            news.set_site('tuoitre.vn')
    elif 'vnexpress.net' in url:
        vne = VNExpress(url)
        vne.get()
        if log:
            vne.print_log()
        if vne.is_valid():
            news = vne.get_news()
            news.set_site('vnexpress.net')
    elif 'dantri.com.vn' in url:
        dt = Dantri(url)
        dt.get()
        if log:
            dt.print_log()
        if dt.is_valid():
            news = dt.get_news()
            news.set_site('dantri.com.vn')
    return news


def parse_rss_url(rss_urls, crawled, log):
    datas = []
    links = {}
    try:
        for rss_url in rss_urls:
            json_data = feedparser.parse(rss_url)
            for item in json_data['entries']:
                try:
                    url = item['link']
                    links[url] = True
                    if url not in crawled:
                        create_date = item['published']
                        news = call_crawler(url, log)
                        if news:
                            news.set_create_date(create_date)
                            datas.append(news)
                except:
                    traceback.print_exc()
                    pass
    except:
        traceback.print_exc()
    return datas, links


def read_crawled(crawled_file):
    try:
        with open(crawled_file, encoding='utf8') as fp:
            return json.load(fp)
    except FileNotFoundError:
        pass
    except:
        traceback.print_exc()
    return {}


def save_crawled(crawled, save_path):
    with open(save_path, 'w', encoding='utf8') as fp:
        json.dump(crawled, fp, ensure_ascii=False)


class RssParser:
    def __init__(self, rss_urls, crawled_file='', log=True):
        self._rss_urls = rss_urls
        self.__crawled = read_crawled(crawled_file)
        self.__rss_data, self.__crawled = parse_rss_url(self._rss_urls, self.__crawled, log)
        save_crawled(self.__crawled, crawled_file)

    def get_data(self, filename=None):
        if filename:
            with open(filename, 'w', encoding='utf8') as fp:
                json.dump(self.__rss_data, fp, ensure_ascii=False)
        return self.__rss_data


if __name__ == '__main__':
    rss = RssParser(['https://vnexpress.net/rss/tin-moi-nhat.rss',
                     'https://dantri.com.vn/rss/tin-moi-nhat.rss',
                     'https://tuoitre.vn/rss/tin-moi-nhat.rss'],
                    log=True, crawled_file='stored/crawled.json')
    lst = rss.get_data()
    print(len(lst))
